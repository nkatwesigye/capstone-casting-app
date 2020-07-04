# FSND Casting Agency Capstone project

## Capstone project for the udacity full stack  Developer nanodegree program.

**Heroku link:** (https://ud-casting-app.herokuapp.com/)

### The project implements RBAC using auth0, to login or set up an account, go to the following url: 

https://dev-4762mi-b.us.auth0.com/authorize?response_type=token&client_id=FQqOCOlHtV3tU4qZsvfMRcpi8R52YDKp&redirect_uri=https://ud-casting-app.herokuapp.com/movies&audience=https://casting/

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in api.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

To run the server, execute:

```
export FLASK_APP=app
export FLASK_ENV=development
flask run 
```


## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Models

Movies with attributes contain id, title, release_date, actor_id 
Actors with attributes id , name, age and gender

## Environment Variables

In the `.env` file, the JWT token for each User Role
- CASTING_ASSISTANT
- CASTING_DIRECTOR
- EXECUTIVE_PRODUCER

## Roles

Casting Assistant

- GET:actors
- GET:movies

Casting Director
#####  All permissions a Casting Assistant has
- POST:actor
- DELETE:actor
- PATCH:actor
- PATCH:movie

Executive Producer

##### All permissions a Casting Director has
- POST:movie
- DELETE:movie

## Endpoints

Fetches all the actors in the database and returns a json object
`````bash
GET '/actors'

reponse = {
    "actors": [
        {
            "age": 22,
            "gender": "Male",
            "id": 1,
            "name": "John Doe"
        },
        {
            "age": 22,
            "gender": "Male",
            "id": 2,
            "name": "John Doe"
        },
        {
            "age": 22,
            "gender": "Male",
            "id": 3,
            "name": "John Doe"
        },
        {
            "age": 22,
            "gender": "Male",
            "id": 4,
            "name": "John Doe"
        },
`````
This endpoint will create a new actor in the database based on the json that is in the body of the request, returns actor added 

`````bash
POST '/actors'

payload = {
  "actor_age": 22,
  "actor_gender": "Male",
  "actor_name": "John Doe"
}
",
  }
response = {
    "added_actors": {
        "age": 22,
        "gender": "Male",
        "id": 13,
        "name": "John Doe"
    },
    "success": true
}

`````
This endpoint will modify the actor that corresponds to the actor ID that is passed into the url based on the json payload  that is passed into the body of the request, returns added actor

`````bash
PATCH '/actors/<int:actor_id>'

params = <int:actor_id>

payload = {
  "new_actor_name" :"Masters",
  "new_actor_age" : 30
              }

response = {
    "all_actors": [
        {
            "age": 22,
            "gender": "Male",
            "id": 1,
            "name": "John Doe"
        },
        {
            "age": 30,
            "gender": "Male",
            "id": 5,
            "name": "Masters"
        }
    ],
    "success": true
}

`````
This endpoint will delete the actor that corresponds to the actor ID that is passed into the url, returns id of deleted actor
`````bash
DELETE '/actors/<int:actor_id>'

params = <int:actor_id>

response = {
    "deleted": 6,
    "success": true
}

`````
Fetches all the movies in the database and returns a json object

`````bash
GET '/movies'

response = {
    "movies": [
        {
            "actor_name": "John Doe",
            "id": 1,
            "movie_name": "New Movie",
            "release_date": "01-02-2021"
        },
        {
            "actor_name": "John Doe",
            "id": 2,
            "movie_name": "New Movie",
            "release_date": "01-02-2021"
        }
    ],
    "success": true,
    "total_movies": 2
}
`````

This endpoint will create a new movie in the database based on the json that is in the body of the request, returns movie added 

`````bash
POST '/movies'

payload = {
    "movie_name": "New Movie",
    "release_date" : "01-02-2021",
    "actor_id": 1
}

response = {
    "added_movie": {
        "actor_id": 1,
        "id": 2,
        "movie_title": "New Movie",
        "release_date": "01-02-2021"
    },
    "success": true
`````
This endpoint will modify the movie that corresponds to the movie ID that is passed into the url based on the json payload  that is passed into the body of the request, returns added movie

`````bash
PATCH '/movies/<int:movie_id>'

params = <int:movie_id>

payload = {
"new_movie_name":"Big5",
"new_release_date": "05-06-2013"
     }

response = {
    "all_movies": [
        {
            "actor_id": 1,
            "id": 1,
            "movie_title": "New Movie",
            "release_date": "01-02-2021"
        },
        {
            "actor_id": 1,
            "id": 2,
            "movie_title": "Big5",
            "release_date": "05-06-2013"
        }
    ],
    "success": true
`````
This endpoint will delete the actor that corresponds to the movie ID that is passed into the url, returns id of deleted movie

`````bash
DELETE '/movies/<int:movie_id>'


params = <int:movie_id>

response = {
    "deleted": 2,
    "success": true
}

`````
## Unit Testing

To run unit tests,run in your terminal

```bash

python3 test_app.py
`````
