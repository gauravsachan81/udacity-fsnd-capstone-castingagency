import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, setup_migrations
from auth import requires_auth, AuthError

'''
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  return app
'''


def create_app():
    # Create and Configure the app
    app = Flask(__name__)
    # Connect APP with DB
    setup_db(app)
    setup_migrations(app)

    # APP home route
    @app.route('/')
    def health_check():
        return jsonify({"success": True, "message": "Home Route is Healthy!!"})

    # Actors route #############

    # GET (SELECT) all actors
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_all_actors():
        s_actors = []
        try:
            actors = Actor.query.order_by(Actor.actor_id).all()
            s_actors = [a.serialized_actor() for a in actors]
        except Exception as e:
            print("Error happened in GET all actors", e)
        if len(s_actors) == 0:
            print("There are yet no actors in the DB !!")
            abort(404)
        return jsonify({"success": True, "actors": s_actors})

    # DELETE an actor
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(actor_id):
        del_actor = Actor.query.get(actor_id)
        if del_actor is None:
            print("No such actor to DELETE", actor_id)
            abort(404)
        try:
            del_actor.delete()
        except Exception as e:
            print("Error occured during DELETE, check with developer", e)
            abort(422)
        return jsonify({"success": True, "id": actor_id})

    # POST (INSERT) an actor
    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_new_actor():
        req_body = request.get_json()
        name = req_body.get("name", None)
        age = req_body.get("age", None)
        gender = req_body.get("gender", None)
        if name is None or age is None or gender is None:
            print("Either of Name or Age or Gender is not provided")
            abort(400)
        else:
            try:
                s_actor = Actor(name=name, age=age, gender=gender)
                s_actor.insert()
            except Exception as e:
                print("Error occured during INSERT, check with developer", e)
                abort(422)
        return jsonify(
            {
                "success": True, "actors": s_actor.serialized_actor()
            }
        )

    # PATCH (UPDATE) an actor
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(actor_id):
        upd_actor = Actor.query.get(actor_id)
        if upd_actor is None:
            print("No actor found to update")
            abort(404)
        try:
            req_body = request.get_json()
            name = req_body.get("name", None)
            age = req_body.get("age", None)
            gender = req_body.get("gender", None)
            if name is not None:
                upd_actor.name = name
            if age is not None:
                upd_actor.age = age
            if gender is not None:
                upd_actor.gender = gender
            upd_actor.update()
        except Exception as e:
            print("Error occured during UPDATE, check with developer", e)
            abort(422)
        return jsonify({"Patch success": True,
                        "actor": upd_actor.serialized_actor()})

    # Movies route #############

    # GET (SELECT) all movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_all_movies():
        s_movies = []
        try:
            movies = Movie.query.order_by(Movie.movie_id).all()
            s_movies = [m.serialized_movie() for m in movies]
        except Exception as e:
            print(e)
        if len(s_movies) == 0:
            print("There are yet no movies in the DB !!")
            abort(404)
        return jsonify({"success": True, "movies": s_movies})

    # DELETE a movie
    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(movie_id):
        del_movie = Movie.query.get(movie_id)
        if del_movie is None:
            print("No such movie to DELETE", movie_id)
            abort(404)
        try:
            del_movie.delete()
        except Exception as e:
            print("Error occured during DELETE, check with developer", e)
            abort(422)
        return jsonify({"success": True, "movie_id": movie_id})

    # POST (INSERT) a movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_new_movie():
        req_body = request.get_json()
        movie_title = req_body.get("movie_title", None)
        release_date = req_body.get("release_date", None)
        if release_date is None or movie_title is None:
            print("Either of release_date or title is not provided")
            abort(400)
        else:
            try:
                s_movie = Movie(movie_title=movie_title,
                                release_date=release_date)
                s_movie.insert()
            except Exception as e:
                print("Error occured during INSERT, check with developer", e)
                abort(422)
        return jsonify(
            {
                "Post Success": True, "movies": s_movie.serialized_movie()
            }
        )

    # PATCH (UPDATE) a movie
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(movie_id):
        upd_movie = Movie.query.get(movie_id)
        if upd_movie is None:
            abort(404)
        try:
            req_body = request.get_json()
            movie_title = req_body.get("movie_title", None)
            release_date = req_body.get("release_date", None)
            if movie_title is not None:
                upd_movie.movie_title = movie_title
            if release_date is not None:
                upd_movie.release_date = release_date
            upd_movie.update()
        except Exception as e:
            print("Error occured during UPDATE, check with developer", e)
            abort(422)
        return jsonify({"Patch success": True,
                        "movie": upd_movie.serialized_movie()})

    # Error Handlers ###########

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(401)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Not Authorized"
        }), 401

    @app.errorhandler(403)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "message": "Resource not found",
            "error": 404
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(422)
    def not_processable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request cannot be processed"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "error": 500
        }), 500

    # Auth Error Capture
    @app.errorhandler(AuthError)
    def auth_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7070, debug=True)
