import os
from flask import Flask, request, abort, jsonify, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import setupdb, Category, Problem
from forms import QuestionForm
from flask_wtf.csrf import CSRFProtect
from config import SECRET_KEY
import os
csrf = CSRFProtect() 

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  app.secret_key = SECRET_KEY
  setupdb(app)
  CORS(app)
  
  
  
  csrf.init_app(app)

  @app.route('/')
  def index():
    return render_template('index.html')

  @app.route('/categories')
  def categories():
    categories = Category.query.all()
    print(categories) 
    return render_template('categories.html', category_data=categories)

  @app.route('/categories/<int:category_id>/questions')
  def category_questions(category_id):
    current_category = Category.query.get(category_id)
    questions = current_category.problems
    category_name = current_category.category_name
    category_name = category_name.upper()
    print(questions)
    return render_template("questions.html", questions=questions, category=category_name, category_id=category_id)
    
  @app.route('/categories/<int:category_id>/addquestion')
  def create_question(category_id):
    form = QuestionForm()
    category = Category.query.get(category_id)
    category_name = category.category_name
    return render_template('create_question.html', form=form, category_id=category_id, category_name=category_name)

  @app.route('/categories/<int:category_id>/addquestion', methods=['POST'])
  def insert_question(category_id):
    try:
      question_title = request.form['question_title']
      question = request.form['question']
      answer = request.form['answer']
      print(question[0:10])
      print(answer[0:10])
      problem = Problem(question_title=question_title, question=question, answer=answer, cat_id=category_id)
      problem.insert()
    except:
      flash("Error occured during insert")
      print("Error occured")
      abort(400)
    flash("Question successfully added")
    return redirect(url_for('create_question', category_id=category_id))

  return app

APP = create_app()



if __name__ == '__main__':
    #APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(debug=True)