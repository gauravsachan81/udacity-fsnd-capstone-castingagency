# Udacity Full Stack Nanodegree - Capstone Project - Casting Agency

## Casting Agency - Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 
You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Driver for putting up this project

Capstone project of Udacity Fullstack Nanodegree program, allowed demonstration of varied aspects of Fullstack, including but not limited to SQLAlchemy (ORM), Postgres DB, Python Flask library, Auth0 authentication, Gunicorn Webserver and Render platform to develop and deploy APIs. The Capstone project was followed by previous 4 projects which gradually built the concepts by focussed projects, leading upto the Capstone Project which is testing the knowledge on all the topics together.

## Application is hosted at Render
[Casting Agency](https://udacity-fsnd-capstone-castingagency.onrender.com)

## Getting Started

### Installing Dependencies

Python is the main language used in the project.
#### Python 3.7.9
[Python Instllation](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Recommending to work within a Virtual Environment while using Python for creating projects. This helps keeping your package dependencies for each project separate and per project. Instructions for setting up a Virual Enviornment for your platform are noted in [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once Virtual Environment is setup please install dependencies using below command:

pip install -r requirements.txt

The `requirements.txt` file has all required packages required for running the project.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM that is utilized to handle the lightweight sqlite database. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension to handle cross origin requests from our frontend server.

- [Gunicorn](https://gunicorn.org/) The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server. It is a pre-fork worker model, ported from Ruby's Unicorn project.  

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

python app.py


#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login using the crededntials below and replace them in setup.sh and run setup.sh again

.env has the environment variables needed for the project. The app may fail if they are not set properly. Carefully go through the file and make changes as necessary according to your needs.

# Project Deployment Platform - Render

<<Render Link>>

###### To test end points, POSTMAN can be used, the collections file for which can be reffered to.

https://ufsnd.uk.auth0.com/authorize?audience=http://casting-agency-api:5000&response_type=token&client_id=Cip1fgdo5AvJ5B9Th3mtLobdz9vkrI43&redirect_uri=http://localhost:7070/

Casting Assistant 
(
    user       =   casting_assisstant@castingagency.com
    password   =   Noida$2023
)

Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjctM01sbjdLNWV5SnNxM1F5VEhESiJ9.eyJpc3MiOiJodHRwczovL3Vmc25kLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDY1MjEzYmM0MjQ0MTE2MGQwZDA1NzciLCJhdWQiOiJodHRwOi8vY2FzdGluZy1hZ2VuY3ktYXBpOjUwMDAiLCJpYXQiOjE2ODQzOTc4MDYsImV4cCI6MTY4NDQ4NDIwNiwiYXpwIjoiQ2lwMWZnZG81QXZKNUI5VGgzbXRMb2Jkejl2a3JJNDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.GlOnrUfOUH4qHBVAjPDsXnJ6EuRpm36l0ID6kzpVf8xu_Ks1LPw72e6jPM1Y8mTruYBqFev9_pq0io1N9xiBQLJTPL_mgi3ugPtnlz8tncZmqREjLUFeCsR0CS-HtUEmVNyElIiwSqAIgujTw5HriDkfPmCIPWls9lMAydJ_of_RxgzlGQtWLU6TQJiL7yWv_CQXt4ELgpHWsTQJQeNUVL64Maadri21mxNNPepTp4fvqiUKqiH9gQdNgytMPb2iPJY5SkroT85uIL9K3tONqOeowP_GutJfooifRph9aCxFM7rgruDrYdmHnd7YZXRDD-SItXZK6Oqi-W1CcAqzrg
```

Casting director  
(
    user        =   casting_director@castingagency.com
    password    =   Noida$2023
)

Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjctM01sbjdLNWV5SnNxM1F5VEhESiJ9.eyJpc3MiOiJodHRwczovL3Vmc25kLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDY1MjJjODBjNGE4NzdhOGIxNzY2MWQiLCJhdWQiOiJodHRwOi8vY2FzdGluZy1hZ2VuY3ktYXBpOjUwMDAiLCJpYXQiOjE2ODQzOTc5NjEsImV4cCI6MTY4NDQ4NDM2MSwiYXpwIjoiQ2lwMWZnZG81QXZKNUI5VGgzbXRMb2Jkejl2a3JJNDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.WiyGJBRiFWgUV-PORo7XSDZ1swcbDMq2TszICZIIvBjqxf2fndoL15NeAdRGg8MouwU2QNs7nzoeu8G374n0ZNYRZG51_NKDppt-PQ2Mqx43rKITL7-RjJBKU66jllcHlvfLwANToENmi8bZNMOjjnOUY4iGUhFhP8kpggyEfZqeKDt8HQswxT8NEX_sYP6-TK5boo1QCLVcR2JlDMJza_dshgZWjZkiffGZYClSig82ku7grU4-HoWJQXsfRwt2Ri7hSvm8hhUXo69VbWSTbK1MY1Z4mlNC2eQBy_fm-GKpqNjseNnbUtoAsSt8l7T51d9euBkza-fq5RpLrmJAfA
```

Executive Producer 
(
    user        =   casting_executive_producer@castingagency.com
    password    =   Noida$2023
)

Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjctM01sbjdLNWV5SnNxM1F5VEhESiJ9.eyJpc3MiOiJodHRwczovL3Vmc25kLnVrLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDY1MjM0NWM0MjQ0MTE2MGQwZDA1N2UiLCJhdWQiOiJodHRwOi8vY2FzdGluZy1hZ2VuY3ktYXBpOjUwMDAiLCJpYXQiOjE2ODQzOTgwMTcsImV4cCI6MTY4NDQ4NDQxNywiYXpwIjoiQ2lwMWZnZG81QXZKNUI5VGgzbXRMb2Jkejl2a3JJNDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.KcZyl3zS02VYWgKVzgHnezJKV6T2SCophS6pTp9wV9ECemkFv-ICTTCyWFIUc1LH7h5ZLpXtuaoRFxleIDKnR3EbC7qj6n6jJtj2G3_zSuEBqwIvEZJS-nSEdKYJ9T40ggEAmKF45uWSLZP6rZyjE_b5tEnyOylkHcwGmZbSlr_5vWkd_cxReE9VDhUrcBBHvB6LTHKHs_o_0YwJrxez2QBy7n4cd2VT9uGy7ggMFOsMC0qOr0DVT7sGDCHAE3e-BIHhEXTk-LLdq3nsuQfeBrimhE_ZSSWGg_aYofL9wgkXUj8yHW-QOyhPGgZPIk8FMEgCxoW0Oj0CWozT21He0A
```

## Testing

To run the tests locally, run

python test_app.py

## API Reference

### Endpoints

GET '/actors'
POST '/actors'
PATCH '/actors/<actor_id>'
DELETE '/actors/<actor_id>'
GET '/movies'
POST '/movies'
PATCH '/movies/<movie_id>'
DELETE '/movies/<movie_id>'
----------------------------------------------------------------------------------

GET '/actors'
Gets all the actors present in the database
URL Argument                : None
Data Arguments              : None
Returns                     : json with all the actor ID,name, age and gender 
Sample successful response  :

```
{
    "actors": [
        {
            "age": 42,
            "gender": "male",
            "id": 1,
            "name": "Sachan"}
        ],
    "success": true    
}
```

POST '/actors'
Create a new actor in the database
URL Argument                : None
Data Arguments              : age, name, gender
Sample Input                :
```
{
    "age":42,
    "name": "Gaurav",
    "gender": "male"
}
```
Returns                     : json with the ID,name, age and gender 
Sample successful response  :
```
{
    "actors": {
        "age": 42,
        "gender": "male",
        "id": 2,
        "name": "Gaurav"
    },
    "success": true
}
```

Patch '/actors/<actor_id>'
Update an actor already in the database
URL Argument                : Actor id
Data Arguments              : age or/and name or/and gender
Sample Input                :
```
{
    "gender": "male",
    "name": "Amitabh B",
    "age":76
}
```
Returns : Json with actor ID,name, age and gender 
Sample successful response:
```
{
    "actor": {
        "age": 76,
        "gender": "male",
        "id": 2,
        "name": "Gaurav Sachan"
    },
    "success": true
}
```
Delete '/actors/<actor_id>'
Delete an actor from the database
URL Argument                : Actor id
Data Arguments              : None
Returns                     : json with all the id of the actor which is deleted
Sample successful response  :
```
{
    "id": 2,
    "success": true
}
```

GET '/movies'
Gets all the movies present in the database
URL Argument                : None
Data Arguments              : None
Returns                     : json with all the title, id and release date
Sample successful response:

```
{
    "movies": [
        {
            "id": 3,
            "release_date": "2009-10-10",
            "title": "Kaun"
        } ],
    "success": true
}
```

POST '/movies'
Create a new movie in the database
URL Argument                : None
Data Arguments              : title, release date
Sample Input :
```
{
    "title": "Don",
    "release_date":"1988-10-10"
}
```
Returns                     : json with the ID,name, age and gender 
Sample successful response:
```
{
    "movies": {
        "id": 9,
        "release_date": "1998-10-10",
        "title": "Don"
    },
    "success": true
}
```

Patch '/movies/<movie_id>'
Update a movie already in the database
URL Argument                : Movie id
Data Arguments              : title and/or release date
Sample Input                :
```
{
    "title": "The Gone Case",
    "release_date" : "2005-06-01"
}
```
Returns : Json with ID,release date and title
Sample successful response:
```
{
    "movie": {
        "id": 5,
        "release_date": "2005-06-01",
        "title": "The Gone"
    },
    "success": true
}
```
Delete '/movies/<movie_id>'
Delete a movie from the database
URL Argument                : movie id
Data Arguments              : None
Returns                     : json with id
Sample successful response:
```
{
    "id": 1,
    "success": true
}
```

Please Note : Sample data above does not reflect the data in collections file, and should just be treaded as sample.

### Error Handling

Errors are returned as json objects. 
Sample format :

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}

```

## Authors and key contributors

Author      :       Gaurav Sachan
