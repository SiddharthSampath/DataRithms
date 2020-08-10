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

# route to set the header with the bearer token once a user logs in
  @app.route('/setheader/')
  def setHeader():
    header = request.headers.get('Authorization')
    if header is not None:
      session['token'] = header
    return jsonify({"Success" : True, "header" : header})
  
# redirecting on successful login
  @app.route('/login/')
  def login(): 
    return render_template('login.html')

# Removing token from session once user logs out
  @app.route('/logout/')
  def logout(): 
    if 'token' in session:
      session.pop('token')
    flash("You have successfully logged out!")
    return redirect(url_for('index'))

# Returning list of categories
  @app.route('/categories/')
  def categories():
    categories = Category.query.all()
    return render_template('categories.html', category_data=categories)

# Returning questions per category
  @app.route('/categories/<int:category_id>/questions/')
  def category_questions(category_id):
    current_category = Category.query.get(category_id)
    questions = current_category.problems
    category_name = current_category.category_name
    category_name = category_name.upper()
    return render_template("questions.html", questions=questions, category=category_name, category_id=category_id)
    
# Route to return form to be displayed
  @app.route('/categories/<int:category_id>/addquestion/')
  @requires_auth('post:question')
  def create_question(payload,category_id):
    form = QuestionForm()
    category = Category.query.get(category_id)
    category_name = category.category_name
    return render_template('create_question.html', form=form, category_id=category_id, category_name=category_name)

# Route to handle the form data sent to the backend
  @app.route('/categories/<int:category_id>/addquestion/', methods=['POST'])
  @requires_auth('post:question')
  def insert_question(payload, category_id):
    try:
      question_title = request.form['question_title']
      question = request.form['question']
      answer = request.form['answer']
      problem = Problem(question_title=question_title, question=question, answer=answer, cat_id=category_id)
      problem.insert()
      flash("Question successfully added")
    except:
      rollback()
      flash("Error occured during insert")
      abort(400)
    
    
    return redirect(url_for('create_question', category_id=category_id))

# Route to return edit form
  @app.route('/questions/<int:question_id>/edit')
  def edit_question_display(question_id):
    question = Problem.query.get(question_id) 
    form = QuestionForm(obj=question)
    return render_template('edit_question.html', form=form)

# Route to handle to edited information
  @app.route('/questions/<int:question_id>/edit', methods=['PATCH', 'POST'])
  @requires_auth('patch:question')
  def edit_question(payload,question_id): 
    try:
      question_title = request.form['question_title']
      question = request.form['question']
      answer = request.form['answer']
      problem = Problem.query.get(question_id)
      problem.question_title = question_title
      problem.question = question
      problem.answer = answer
      problem.insert()
      category_id = problem.cat_id
      flash("Question successfully edited")
    except:
      rollback()
      flash("Error occured during edit")
      abort(400)
    
    
    return redirect(url_for('category_questions', category_id=category_id))

# Route to handle delete requests sent
  @app.route('/questions/<int:question_id>/delete', methods=['DELETE','GET'])
  @requires_auth('delete:question')
  def delete_question(payload,question_id):
    try:
      question = Problem.query.get(question_id)
      category_id = question.cat_id
      question_id = question.id
      question.delete()
      flash("Question successfully deleted!") 
    except:
      rollback()
      flash("Question could not be deleted")
      abort(400)
    
    
    return redirect(url_for('category_questions', category_id=category_id))

# Route to render form for add category
  @app.route('/categories/addcategory/')
  def create_category():
    form = CategoryForm()
    return render_template('create_category.html', form=form)
  
# Route to handle add category data
  @app.route('/categories/addcategory/', methods=['POST'])
  @requires_auth('post:category')
  def insert_category(payload):
    try: 
      category_name = request.form['category_name'] 
      category_description = request.form['category_description']
      category = Category(category_name=category_name, category_description=category_description)
      category.insert() 
      flash("Category added successfully")
    except:
      flash("Error occurred during insert")
      rollback()
      abort(422)
    
    return redirect(url_for('create_category'))

# Error handlers

  @app.errorhandler(404)
  def notFound(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "Resource Not Found"
      }), 404


  @app.errorhandler(400)
  def badRequest(error):
      return jsonify({
          "success": False,
          "error": 400,
          "message": "Bad Request"
      }), 400


  @app.errorhandler(401)
  def unauthorized(error):
      return jsonify({
          "success": False,
          "error": 401,
          "message": "Unauthorized"
      }), 401


  @app.errorhandler(403)
  def forbidden(error):
      return jsonify({
          "success": False,
          "error": 403,
          "message": "Permission to perform action not present"
      }), 403
  
  @app.errorhandler(500)
  def servererror(error):
      return jsonify({
          "success": False,
          "error": 500,
          "message": "Server Error"
      }), 403
 
  return app

app = create_app()



if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=8080, debug=True)
    app.run()