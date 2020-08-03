import os
from flask import Flask, request, abort, jsonify, render_template, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import setupdb, Category, Problem, rollback
from forms import QuestionForm, CategoryForm
from flask_wtf.csrf import CSRFProtect
from config import SECRET_KEY
from auth.auth import AuthError, requires_auth
import os
csrf = CSRFProtect() 

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  app.secret_key = SECRET_KEY
  setupdb(app)
  CORS(app,expose_headers='Authorization')
  csrf.init_app(app)
  
  
  
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,PUT,DELETE,OPTIONS')
    return response

  @app.route('/')
  def index():
    return render_template('index.html')

  @app.route('/setheader/')
  def setHeader():
    header = request.headers.get('Authorization')
    if header is not None:
      session['token'] = header
    print(f"Session Token : {session['token']}")
    return jsonify({"Success" : True, "header" : header})
  @app.route('/login/')
  def login(): 
    
    return render_template('login.html')

  @app.route('/categories/')
  def categories():
    
    print(f"Headers = {request.headers.get('Authorization')}")  
    categories = Category.query.all()
    print("Hey there") 
    return render_template('categories.html', category_data=categories)
   
  @app.route('/categories/<int:category_id>/questions/')
  def category_questions(category_id):
    current_category = Category.query.get(category_id)
    questions = current_category.problems
    category_name = current_category.category_name
    category_name = category_name.upper()
    print(questions)
    return render_template("questions.html", questions=questions, category=category_name, category_id=category_id)
    
  @app.route('/categories/<int:category_id>/addquestion/')
  def create_question(category_id):
    form = QuestionForm()
    category = Category.query.get(category_id)
    category_name = category.category_name
    return render_template('create_question.html', form=form, category_id=category_id, category_name=category_name)

  @app.route('/categories/<int:category_id>/addquestion/', methods=['POST'])
  @requires_auth('post:question')
  def insert_question(payload, category_id):
    try:
      question_title = request.form['question_title']
      question = request.form['question']
      answer = request.form['answer']
      print(question[0:10])
      print(answer[0:10])
      problem = Problem(question_title=question_title, question=question, answer=answer, cat_id=category_id)
      problem.insert()
    except:
      rollback()
      flash("Error occured during insert")
      print("Error occured")
      abort(400)
    
    flash("Question successfully added")
    return redirect(url_for('create_question', category_id=category_id))

  @app.route('/categories/addcategory/')
  def create_category():
    form = CategoryForm()
    return render_template('create_category.html', form=form)
  
  @app.route('/categories/addcategory/', methods=['POST'])
  @requires_auth('post:category') 
  def insert_category(payload):
    try:
      category_name = request.form['category_name']
      category_description = request.form['category_description']
      category = Category(category_name=category_name, category_description=category_description)
      category.insert()
    except:
      flash("Error occurred during insert")
      rollback()
    flash("Category added successfully")
    return redirect(url_for('create_category'))



  return app

APP = create_app()



if __name__ == '__main__':
    #APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(debug=True)