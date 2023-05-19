from dotenv import load_dotenv
import os
# Creating separate .env file test and main
if os.environ.get("env") == "test":
    load_dotenv(".env.test")
else:
    load_dotenv(".env")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
ASSISTANT_TOKEN = os.environ.get("ASSISTANT_TOKEN")
DIRECTOR_TOKEN = os.environ.get("DIRECTOR_TOKEN")
PRODUCER_TOKEN = os.environ.get("PRODUCER_TOKEN")
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
API_AUDIENCE = os.environ.get("API_AUDIENCE")
ALGORITHMS = os.environ.get("ALGORITHMS")
