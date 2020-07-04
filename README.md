# FSND Casting Agency Capstone project

## capstone project for the udacity full stack nanodegree program.

**Heroku link:** (https://ud-casting-app.herokuapp.com/)

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

`````bash
Fetches all the actors in the database and returns a json object
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

PATCH '/actors/<int:actor_id>'

params = <int:actor_id>

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

DELETE '/actors/<int:actor_id>'

params = <int:actor_id>

response = {
    "deleted": 6,
    "success": true
}

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


DELETE '/movies/<int:movie_id>'


params = <int:movie_id>

response = {
    "deleted": 2,
    "success": true
}

`````


There are three roles within the API. Casting Assistant, Casting Director and Executive Producer. The logins for the three roles has been provided in the separate notes 

The url for the API:
https://capstone-casting.herokuapp.com/

The endpoints are as follows: 

GET '/movies'
    This endpoint fetches all the movies in the database and displays them as json 

GET '/actors'
    This endpoint fetches all the actors in the databse and displays them as json 

POST '/movies/create'
    This endpoint will create a new movie in the database based on the json that is in the body of the request 

POST '/actors/create'
    This endpoint will create a new actor in the database based on the json that is in the body of the request 

DELETE '/movies/delete/int:movie_id'
    This endpoint will delete the movie that corresponds to the movie ID that is passed into the url 

DELETE '/actors/delete/int:actor_id'
    This endpoint will delete the actor that corresponds to the actor ID that is passed into the url 

PATCH '/actors/patch/int:actor_id' 
    This endpoint will modify the actor that corresponds to the actor ID that is passed into the url based on the json that is passed into the body of the request 

PATCH '/movies/patch/int:movie_id'
    This endpoint will modify the movie that corresponds to the movie ID that is passed into the url based on the json that is passed into the body of the request
## Unit Testing

To run unit tests,run in your terminal

```bash

python3 test.py
`````
