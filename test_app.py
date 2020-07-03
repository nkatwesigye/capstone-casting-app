
import os
import unittest
import json
from flask import Flask, request, abort, jsonify,json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from app import create_app
from flask_cors import CORS
import random
import datetime

from models import setup_db, Movies,Actors
from auth.auth import AuthError, requires_auth


class CastingTestCase(unittest.TestCase):

    def setUp(self):
        '''define test variables and initialize app'''

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_test"
        self.casting_assistant = os.getenv('CASTING_ASSISTANT')
        self.casting_director = os.getenv('CASTING_DIRECTOR')
        self.executive_producer = os.getenv('EXECUTIVE_PRODUCER')
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app,self.database_path)
        
        self.new_movie = {
            'movie_name': 'New Movie',
            'release_date' : '01-02-2021',
            'actor_id': 1,
        }

        self.new_actor = {
            'id': 1,
            'actor_age': 22,
            'actor_gender': 'Male',
            'actor_name': 'John Doe',
        }

        self.movie_patch = {
            'new_movie_name': 'Big5',
            'new_release_date': '05-06-2013'
             }

        self.actor_patch = {
               'new_actor_name' :'Masters',
               'new_actor_age' : 30,
              }
       

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        pass 
       

    def test_fetch_all_actors_casting_assistant(self):
        res = self.client().get('/actors',
                                headers={
                                    "Authorization": "Bearer {}".format(
                                        self.casting_assistant)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        

    def test_fetch_all_movies_casting_assistant(self):
        res = self.client().get('/movies',
                                headers={
                                    "Authorization": "Bearer {}".format(
                                        self.casting_assistant)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    
    def test_create_new_movie_executive_producer(self):
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.executive_producer)
                                 },json=self.new_movie)
        data = json.loads(res.data)
        global movie_id 
        movie_id = data['added_movie']['id']
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['added_movie']['movie_title'],'New Movie'),
        self.assertEqual(data['added_movie']['release_date'], '01-02-2021')
        self.assertEqual(data['added_movie']['actor_id'], 1)

    def test_patch_actor_executive_producer(self):
         res = self.client().patch('/actors/'+ str(actor_id),
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.executive_producer)
                                 },json=self.actor_patch)
         data = json.loads(res.data)
         self.assertEqual(res.status_code, 200)
         self.assertEqual(data['success'], True)

    def test_create_new_movie_casting_assistant(self):
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_assistant)
                                 }, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
    
    def test_create_new_actor_casting_assistant(self):
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_assistant)
                                 }, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_create_new_actor_casting_director(self):
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_director)
                                 },json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['added_actors']['age'], 22),
        self.assertEqual(data['added_actors']['name'], 'John Doe')
        self.assertEqual(data['added_actors']['gender'], 'Male')
        global actor_id 
        actor_id = data['added_actors']['id']
                            
    def test_create_new_movie_casting_director(self):
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_director)
                                 },json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_movie_casting_director(self):
        res = self.client().delete('/movies/'+ str(movie_id),
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_director)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()