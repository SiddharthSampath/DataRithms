import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import setupdb, Category, Problem

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setupdb(app)
  CORS(app)

  return app

APP = create_app()

@APP.route('/')
def index():
  return render_template('index.html')

@APP.route('/categories')
def categories():
  categories = Category.query.all()
  print(categories) 
  return render_template('categories.html', category_data=categories)

@APP.route('/categories/<int:category_id>/questions')
def category_questions(category_id):
  current_category = Category.query.get(category_id)
  questions = current_category.problems
  category_name = current_category.category_name
  category_name = category_name.upper()
  print(questions)
  return render_template("questions.html", questions=questions, category=category_name)
  

if __name__ == '__main__':
    #APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(debug=True)