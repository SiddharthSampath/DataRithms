import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import setupdb

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
if __name__ == '__main__':
    #APP.run(host='0.0.0.0', port=8080, debug=True)
    APP.run(debug=True)