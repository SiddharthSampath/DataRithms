import os
from sqlalchemy import Column, String, Integer, Text, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()


def setupdb(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    #db.create_all()

class Problem(db.Model):
    __tablename__ = 'problems'
    id = Column(Integer(), primary_key=True)
    question_title = Column(String(80), nullable=False)
    question = Column(Text(), nullable=False)
    answer = Column(Text(), nullable=False)
    cat_id = Column(Integer(), ForeignKey('categories.id'))

class Category(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key=True)
    category_name = Column(String(), nullable=False)
    category_description = Column(String(), nullable=False)
    problems = relationship('Problem', lazy='dynamic', backref='category', cascade='all, delete-orphan')




