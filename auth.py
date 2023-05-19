import json
import os
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen

# Declare OS Environment parameters
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
ALGORITHMS = os.environ.get("ALGORITHMS")
API_AUDIENCE = os.environ.get("API_AUDIENCE")

# AuthError Exception
# A standardized way to communicate auth failure modes ########


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# Auth Header ########


def get_token_auth_header():
    head = request.headers.get('Authorization', None)

    # Checking if  request has an authorization header
    if head is None:
        raise AuthError({'status': 'Auth_Header_Not_Available',
                         'description': 'Authorization Header should be present.'}, 401)

    auth = head.split()

    # Checking if request has bearer in the auth header
    if auth[0].upper() != 'BEARER':
        raise AuthError({
            'status': 'Auth_Bearer_Not_Found',
            'description': 'Bearer should be included in the Authorization header'}, 401)

    # Checking if request has token in the auth header
    elif len(auth) == 1:
        raise AuthError({
            'status': 'Auth_Token_Not_Found',
            'description': 'Authorization Token should be included in the Authorization header'}, 401)
    # Returning the token
    return auth[1]

# Validating correct persmissions in the Json Web Token
# to implement Role Based Acces Control (RBAC)


def check_permissions(permission, payload):
    if ('permissions' not in payload) or (permission not in payload['permissions']):
        raise AuthError({'status': 'Unauthorized', 'description': 'Required permissions Not found'}, 403)
    return True


# Verifying JWT token
def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    head = jwt.get_unverified_header(token)
    if 'kid' not in head:
        raise AuthError({'status': 'invalid_header', 'description': 'Kid is not present in the JWT header'}, 401)

    key_rsa = None

    for key in jwks['keys']:
        if key['kid'] == head['kid']:
            key_rsa = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    if key_rsa is None:
        raise AuthError({
            'status': 'invalid_header', 'description': 'Keys not present'}, 401)

    try:
        decoded_token = jwt.decode(token,
                                   key=key_rsa,
                                   algorithms=ALGORITHMS,
                                   audience=API_AUDIENCE,
                                   issuer='https://' + AUTH0_DOMAIN + '/')
        return decoded_token

    except Exception:
        raise AuthError({
            'status': 'invalid_header',
            'description': 'Unable to parse authentication token.'
        }, 400)

    except jwt.ExpiredSignatureError:
        raise AuthError({'status': 'expired_token', 'description': 'Token expired.'}, 401)

    except jwt.JWTClaimsError:
        raise AuthError({
            'status': 'invalid_claims',
            'description': 'Incorrect claims. Please, check the audience and issuer.'}, 401)

# Return the decorator which passes the decoded payload to the
# decorated method Decorator function to add authorization to endpoints


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # extract token
            jwt_token = get_token_auth_header()
            # token verfication
            payload = verify_decode_jwt(jwt_token)
            check_permissions(permission, payload)
            return f(*args, **kwargs)
        return wrapper
    return requires_auth_decorator
