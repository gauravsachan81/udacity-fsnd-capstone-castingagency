import os
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_utils import database_exists, create_database
from settings import DB_NAME, DB_USER, DB_PASSWORD


db = SQLAlchemy()

# Get Database URL from the environment variable
DATABASE_URI=os.environ.get("DATABASE_URL")
print("From ENV Variable - Database URI =", DATABASE_URI)

# Setting up Database URI in correct format to align with the dialect
if DATABASE_URI is None:
    DATABASE_URI = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, 'localhost', DB_NAME)
    print("Inside IF - Database URI =", DATABASE_URI)
else:
    DATABASE_URI=DATABASE_URI.replace("://", "ql://", 1)
    print("Inside ELSE - Database URI =", DATABASE_URI)

# Setting up DB config using path
def setup_db(app, database_path=DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    print("Setting up DB config using path")
    
    # Creating DB if it doesn't already exist
    if not database_exists(DATABASE_URI):
        create_database(DATABASE_URI)
        print("Creating DB if it doesn't already exist")

    db.app = app
    db.init_app(app)

def setup_migrations(app):
    migrate = Migrate(app, db)

# DROP and CREATE tables for test
def create_tables_for_test():
    db.drop_all()
    db.create_all()

# Model Class 1 - Movie
class Movie(db.Model):
    __tablename__ = 'movies'  # set table name
    movie_id = db.Column(db.Integer(), primary_key=True)
    movie_title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # serialized movie data to return as json
    def serialized_movie(self):
        return {
                "movie_id": self.movie_id,
                "movie_title": self.movie_title,
                # function to return a string of date, time, and UTC offset to the corresponding time zone in ISO 8601 format.
                "release_date": self.release_date.isoformat()
                }

    def __repr__(self):
        return f'Movie details : {self.movie_id} {self.title}'

# Model Class 2 - Actor
class Actor(db.Model):
    __tablename__ = 'actors'  # set table name
    actor_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Serialized actor data to return as json
    def serialized_actor(self):
        return (
            {"actor_id": self.actor_id,
             "name": self.name,
             "age": self.age,
             "gender": self.gender}
        )

    def __repr__(self):
        return f'Actor Details: {self.actor_id}, {self.name}'
