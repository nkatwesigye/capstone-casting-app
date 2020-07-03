import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "casting"
database_url= os.environ['DATABASE_URL']
database_path = "postgres://{}/{}".format(database_url, database_name)

db = SQLAlchemy()
#migrate = Migrate(app,db)
#setup_db(app)

'''
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_url):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #db.create_all()


class Actors(db.Model):  
  __tablename__ = 'actors'
  id     = Column(Integer, primary_key=True)
  name   = Column(String)
  age    = Column(Integer)
  gender = Column(String)
  movies = db.relationship('Movies',backref='Actors', lazy = True)

  def __init__(self,name,age,gender):
    self.name = name
    self.age  = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender,
    }

class Movies(db.Model):  
  __tablename__ = 'movies'

  id            = Column(Integer, primary_key=True)
  title         = Column(String)
  release_date  = Column(String)
  actor_id      =  db.Column(db.Integer,db.ForeignKey(Actors.id),nullable = False)

  
#venue_id = db.Column(db.Integer,db.ForeignKey(Venue.id),nullable = False)
  

  def __init__(self,title,release_date,actor_id):
    self.title = title
    self.release_date = release_date
    self.actor_id = actor_id

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'movie_title': self.title,
      'release_date': self.release_date,
      'actor_id': self.actor_id,
    }





