import os
import json
import unittest
from ast import Pass
from datetime import datetime
from models import DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from models import db, setup_db, create_tables_for_test, Movie, Actor
from app import create_app

# Setup Environment variable to "test"
# os.environ["env"]="test"

ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')

print(ASSISTANT_TOKEN)
print(DIRECTOR_TOKEN)
print(PRODUCER_TOKEN)

######## Class for testing Actors ########
class ActorsTestCase(unittest.TestCase):
    print("This class includes some test cases for Actors API endpoints")
    
    def setUp(self):
        self.assistant = ASSISTANT_TOKEN
        self.director = DIRECTOR_TOKEN
        self.producer = PRODUCER_TOKEN
        self.app=create_app()
        self.client = self.app.test_client()
        setup_db(self.app)
        with self.app.app_context():
            create_tables_for_test()
    
    ############## Negative Test Case for Actor ##############
    def test_get_actors_negative(self):
        response=self.client.get("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response.data)
        self.assertFalse(response_data['success'],"Success attribute of response json = True")
        self.assertEqual(int(response_data['error']),404,"Error code is not 404")

    ############## Post Test Case for Actor ##############
    def test_post_an_actor(self):
        t_actor = {"name":"Sachan", "age":42,"gender":"male"}
        print("t_actor set")
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        print("response set")
        response_data=json.loads(response.data)
        print("response_data set")
        self.assertTrue(response_data['success'],"Success attribute of response json = False")
        i_actor=Actor.query.get(response_data['actors']['actor_id'])
        t_actor["actor_id"]=response_data['actors']['actor_id']
        self.assertEqual(i_actor.serialized_actor(),t_actor,"Actor in test case and the actor posted in DB are not same")

    ############## Get Test Case for Actors ##############
    def test_get_actors_postitive(self):
        t_actor = {"name":"VK", "age":36,"gender":"male"}
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        response=self.client.get("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response.data)
        self.assertTrue(response_data['success'],"Success attribute of response json = False")
        self.assertGreaterEqual(len(response_data['actors']),1,"Actors are not getting returned")        

    ############## Post Test Case for Actor - Negative ##############
    def test_post_an_actor_negative(self):
        t_actor = {"age":24,"gender":"female"}
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        response_data=json.loads(response.data)
        self.assertFalse(response_data['success'],"Success attribute in response json = False")
        self.assertEqual(int(response_data['error']),400,"Error code is not 400")

    ############## Update Test Case for Actor ##############
    def test_patch_an_actor(self):
        t_actor = {"name":"GS", "age":42,"gender":"male"}
        response=self.client.post("/actors",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 },json=t_actor)
        actor_id=json.loads(response.data)['actors']['actor_id']
        t_actor_upd = {"name":"Sachan"}
        response_upd=self.client.patch(f'/actors/{actor_id}',json=t_actor_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        t_actor["name"]=t_actor_upd['name']
        t_actor["actor_id"]=actor_id
        self.assertEqual(response_data["actor"],t_actor,"Actor in test case and the actor posted in DB are not same")

    ############## Update Test Case for Actor - Negative ##############    
    def test_patch_an_actor_negative(self):
        actor_id=123456789
        t_actor_upd = {"name":"Sachan"}
        response_upd=self.client.patch(f'/actors/{actor_id}',json=t_actor_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertFalse(response_data['success'],"success attribute in response json was true")
        self.assertEqual(int(response_data['error']),404,"error code is not 404")

    ############## Delete Test Case for Actor ##############
    def test_delete_an_actor(self):
        t_actor = {"name":"GS", "age":42,"gender":"male"}
        response=self.client.post("/actors",json=t_actor,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        actor_id=json.loads(response.data)['actors']['actor_id']
        response_upd=self.client.delete(f'/actors/{actor_id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        self.assertEqual(response_data['actor_id'],actor_id,"Actor inserted hasn't been deleted")
    
    ############## Delete Test Case for Actor - Negative ##############
    def test_delete_an_actor_negative(self):
        actor_id=123456789
        response_upd=self.client.delete(f'/actors/{actor_id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertFalse(response_data['success'],"success attribute in response json was true")
        self.assertEqual(int(response_data['error']),404,"error code is not 404")

######## Class for testing Movies ########

class MoviesTestCase(unittest.TestCase):
    print("This Class includes some testcases for Movies API endpoints")

    def setUp(self):
        self.assistant = ASSISTANT_TOKEN
        self.director = DIRECTOR_TOKEN
        self.producer = PRODUCER_TOKEN
        self.app = create_app()
        self.client = self.app.test_client()
        setup_db(self.app)
        with self.app.app_context():
            create_tables_for_test()
    
    def tearDown(self):
        db.session.close()
        Pass

    ############## Get Test Case for Movies ##############
    def test_get_movies_postitive(self):
        t_movie  = {"movie_title":"Terinator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response=self.client.get("/movies",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        self.assertGreaterEqual(len(response_data['movies']),1,"movies are not getting returned") 

    ############## Get Test Case for Movies - Negative ##############
    def test_get_movies_negative(self):
        response=self.client.get("/movies",headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response.data)
        self.assertFalse(response_data['success'],"success attribute in response json was True")
        self.assertEqual(int(response_data['error']),404,"error code is not 404")

    ############## Post Test Case for Movies ##############
    def test_post_a_movies(self):
        t_movie = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        i_movie=Movie.query.get(response_data['movies']['movie_id'])
        t_movie["movie_id"]=response_data['movies']['movie_id']
        self.assertEqual(i_movie.serialized_movie(),t_movie,"Movie in test case and the movie posted in DB are not same")

    ############## Post Test Case for Movies - Negative ##############
    def test_post_a_movie_negative(self):
        t_movie  = {"movie_title":"Terminator"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response.data)
        self.assertFalse(response_data['success'],"success attribute in response json was false")
        self.assertEqual(int(response_data['error']),400,"error code is not 400")

    ############## Update Test Case for Movies ##############
    def test_patch_a_movie(self):
        t_movie  = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        movie_id=json.loads(response.data)['movies']['movie_id']
        t_movie_upd = {"movie_title":"Terminal"}
        response_upd=self.client.patch(f'/movies/{movie_id}',json=t_movie_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        t_movie["movie_title"]=t_movie_upd["movie_title"]
        t_movie["movie_id"]=movie_id
        self.assertEqual(response_data["movie"],t_movie,"Movie in test case and the movie posted in DB are not same")

    ############## Update Test Case for Movies - Negative ##############    
    def test_patch_a_movie_negative(self):
        movie_id=99999
        t_movie_upd = {"movie_title":"The Terminal"}
        response_upd=self.client.patch(f'/movies/{movie_id}',json=t_movie_upd,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertFalse(response_data['success'],"success attribute in response json was true")
        self.assertEqual(int(response_data['error']),404,"error code is not 404")

    def test_delete_a_movie(self):
        t_movie  = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        movie_id=json.loads(response.data)['movies']['movie_id']
        response_upd=self.client.delete(f'/movies/{movie_id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        self.assertEqual(response_data['movie_id'],movie_id,"Movie inserted hasn't been deleted")
    
    def test_delete_a_movie_negative(self):
        movie_id=123456789
        response_upd=self.client.delete(f'/movies/{movie_id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertFalse(response_data['success'],"success attribute in response json was true")
        self.assertEqual(int(response_data['error']),404,"error code is not 404")

############## Auth Test Cases ##############
class AuthTestCase(unittest.TestCase):
    print("This class include testcases for the RBAC auth roles created on Auth0")
    def setUp(self):
        self.assistant = ASSISTANT_TOKEN
        self.director = DIRECTOR_TOKEN
        self.producer = PRODUCER_TOKEN
        self.app=create_app()
        self.client = self.app.test_client()
        setup_db(self.app)
        with self.app.app_context():
            create_tables_for_test()
    
    def tearDown(self):
        db.session.close()

    ############## Auth Test Cases for Producer ##############
    def test_post_a_movies_producer(self):
        t_movie = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        i_movie=Movie.query.get(response_data['movies']['movie_id'])
        t_movie["movie_id"]=response_data['movies']['movie_id']
        self.assertEqual(i_movie.serialized_movie(),t_movie,"Movie in test case and the movie posted in DB are not same")

    def test_delete_a_movie_producer(self):
        t_movie  = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        movie_id=json.loads(response.data)['movies']['movie_id']
        response_upd=self.client.delete(f'/movies/{movie_id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertTrue(response_data['success'],"success attribute in response json was false")
        self.assertEqual(response_data['movie_id'],movie_id,"Movie inserted hasn't been deleted")

    ############## Auth Test Cases for Assisstant ##############
    def test_post_a_movies_assisstant(self):
        t_movie = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.assistant)
                                 })
        response_data=json.loads(response.data)
        self.assertFalse(response_data['success'],"success attribute in response json was True")
        self.assertEqual(int(response_data['error']),403,"error code is not 403")

    def test_delete_a_movie_assisstant(self):
        t_movie  = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        movie_id=json.loads(response.data)['movies']['movie_id']
        response_upd=self.client.delete(f'/movies/{movie_id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.assistant)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertFalse(response_data['success'],"success attribute in response json was True")
        self.assertEqual(int(response_data['error']),403,"error code is not 403")

    ############## Auth Test Cases for Director ##############
    def test_post_a_movies_director(self):
        t_movie = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.director)
                                 })
        response_data=json.loads(response.data)
        self.assertFalse(response_data['success'],"success attribute in response json was True")
        self.assertEqual(int(response_data['error']),403,"error code is not 403")

    def test_delete_a_movie_director(self):
        t_movie  = {"movie_title":"Terminator", "release_date":"2022-12-22"}
        response=self.client.post("/movies",json=t_movie,headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.producer)
                                 })
        movie_id=json.loads(response.data)['movies']['movie_id']
        response_upd=self.client.delete(f'/movies/{movie_id}',headers={
                                     "Authorization": "Bearer {}"
                                     .format(self.director)
                                 })
        response_data=json.loads(response_upd.data)
        self.assertFalse(response_data['success'],"success attribute in response json was True")
        self.assertEqual(int(response_data['error']),403,"error code is not 403")

if __name__ == "__main__":
    unittest.main()