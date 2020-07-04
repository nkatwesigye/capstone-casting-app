import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_cors import CORS
import random
from flask_migrate import Migrate

from models import setup_db, Movies, Actors, db
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r'/*': {'origins': '*'}})

    migrate = Migrate(app, db)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type\
                              ,Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST\
                              ,DELETE, OPTIONS')
        return response

    def get_all_movies():
        movies = []
        all_movies = Movies.query.all()
        for movie in all_movies:
            movies.append(movie.format())
        return movies

    def get_all_actors():
        actors = []
        all_actors = Actors.query.all()
        for actor in all_actors:
            actors.append(actor.format())
        return actors

    # Error Handler
    @app.errorhandler(401)
    def bad_request(error):
        """
        :error handler for error 400
        :param error: Unauthorized
        :return: error: HTTP status code, message: Error description
        """
        return jsonify({
            'success': False,
            'error': 401,
            'message': ' Unauthorized ' + str(error)
        }), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Not Found'
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable Entity'
        })

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello,Your are in public Land"
        if excited == 'true':
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def getactors(payload):
        formated_actors = []
        all_actors = Actors.query.all()
        for actor in all_actors:
            formated_actors.append(actor.format())
        return jsonify({
            'actors': formated_actors,
            'total_actors': len(formated_actors),
            'success': True
            })

    @app.route('/actors', methods=['GET', 'POST'])
    @requires_auth('add:actors')
    def add_actors(payload):
        if request.get_json().get('actor_age'):
            body = request.get_json()
            actor_age = body.get('actor_age')
            actor_gender = body.get('actor_gender')
            actor_name = body.get('actor_name')
            actor = Actors(name=actor_name, age=actor_age, gender=actor_gender)
            actor.insert()
            actor_id = actor.id
            actor_added = Actors.query.filter_by(id=actor_id).first()
        return jsonify({
           'success': True,
           'added_actors': actor_added.format()
        })

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def movies_get(payload):
        formated_movies = []
        dictionarize = {}
        all_movies_with_actor_name = Movies.query.with_entities(Movies.id,
                                                                Movies.title,
                                                                Movies.
                                                                release_date,
                                                                Actors.name).join(Actors, (Movies.actor_id == Actors.id)).all()
        for movies in all_movies_with_actor_name:
            dictionarize['id'] = movies[0]
            dictionarize['movie_name'] = movies[1]
            dictionarize['release_date'] = movies[2]
            dictionarize['actor_name'] = movies[3]
            formated_movies.append(dict(dictionarize))
        return jsonify({
          'movies': formated_movies,
          'total_movies': len(formated_movies),
          'success': True
        })

    @app.route('/movies', methods=['GET', 'POST'])
    @requires_auth('add:movies')
    def movies(payload):
        if request.get_json().get('movie_name'):
            body = request.get_json()
            movie_name = body.get('movie_name')
            release_date = body.get('release_date')
            id_actor = body.get('actor_id')
            movie = Movies(title=movie_name, release_date=release_date,
                           actor_id=id_actor)
            movie.insert()
            movie_id = movie.id
            movie_added = Movies.query.filter_by(id=movie_id).first()
        return jsonify({
             'success': True,
             'added_movie': movie_added.format()
        })

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie_by_id(payload, movie_id):
        movie_by_id = Movies.query.filter_by(id=movie_id).first()
        if movie_by_id is None:
            abort(404)
        try:
            if request.get_json().get('new_movie_name') and request.get_json()\
              .get('new_release_date'):
                body = request.get_json()
                new_title = body.get('new_movie_name')
                new_release_date = body.get('new_release_date')
                movie_by_id.title = new_title
                movie_by_id.release_date = new_release_date
        except ValueError:
            try:
                if request.get_json().get('new_movie_name'):
                    body = request.get_json()
                    new_title = body.get('new_movie_name')
                    movie_by_id.title = new_title
            except ValueError:
                try:
                    if request.get_json().get('new_release_date'):
                        body = request.get_json()
                        new_release_date = body.get('new_release_date')
                        movie_by_id.release_date = new_release_date
                except ValueError:
                    abort(404)
        movie_by_id.update()
        all_movies = get_all_movies()
        return jsonify({
         'success': True,
         'all_movies': all_movies
        })

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor_by_id(payload, actor_id):
        actor_by_id = Actors.query.filter_by(id=actor_id).first()
        if actor_by_id is None:
            abort(404)
        try:
            if request.get_json().get('new_actor_name') and request.get_json()\
              .get('new_actor_age'):
                body = request.get_json()
                new_actor_name = body.get('new_actor_name')
                new_actor_age = body.get('new_actor_age')
                actor_by_id.name = new_actor_name
                actor_by_id.age = new_actor_age
        except ValueError:
            try:
                if request.get_json().get('new_actor_name'):
                    body = request.get_json()
                    new_actor_name = body.get('new_actor_name')
                    actor_by_id.name = new_actor_name
            except ValueError:
                try:
                    if request.get_json().get('new_actor_age'):
                        body = request.get_json()
                        new_actor_name = body.get('new_actor_age')
                        actor_by_id.age = new_actor_age
                except ValueError:
                    abort(404)
        actor_by_id.update()
        all_actors = get_all_actors()
        return jsonify({
         'success': True,
         'all_actors': all_actors
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie_by_id(payload, movie_id):
        movie_by_id = Movies.query.filter_by(id=movie_id).first()
        if movie_by_id is None:
            abort(404)
        movie_by_id.delete()
        return jsonify({
           'success': True,
           'deleted': movie_id
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor_by_id(payload, actor_id):
        actor_by_id = Actors.query.filter_by(id=actor_id).first()
        if actor_by_id is None:
            abort(404)
        try:
            actor_by_id.delete()
        except exc.IntegrityError:
            abort(404)
        return jsonify({
            'success': True,
            'deleted': actor_id
        })

    return app


app = create_app()
if __name__ == '__main__':
    app.run()
