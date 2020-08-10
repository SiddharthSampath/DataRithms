# DataRithms
A web based application, which contains the most popular coding problems, often asked in coding interviews and online coding rounds. The main motivation for this, was to create a platform which would help to just go through all important on a single platform problems and solutions just before an interview. The application is created entirely in Flask, and unittest is used for Unit testing. It uses Auth0 for Role Based Authentication

- Has 3 different roles
-- Admin - The admin creates categories and questions through the frontend. The admin is also allowed to edit and delete questions.

-- Editor - The editor has permissions to edit questions

-- Normal user - The generic user is allowed to view all the categories and questions and their solutions.

## Getting Started
### Tech Stack
> Frontend - mdbootstrap, WTForms, JavaScript

> Backend - Python 3, Flask, SQLAlchemy, PostgreSQL

> Hosting service - Heroku

### Prerequisites
> Python3 and pip should be installed (https://www.python.org/downloads/)

> PostgreSQL should be installed (https://www.postgresql.org/download/)

### Setting up the project to run locally

Create a virtual environment by using the command
> python -m venv venv

Activate the virtual environment
> source venv/Activate/Scripts

To install all the packages required, run the below command from the home directory of the project.
> pip install -r requirements.txt

To use Auth0, an account needs to be created in Auth0.com, and the environment variables need to be modified.

To use environment variables from setup.sh file
> source setup.sh

## Testing

Unittest has been used for testing.

To run the unittests locally, test_db has to be created with the command
> createdb -U postgres test_db

To populate the db with the dump file

>psql -d test_db -U postgres -a -f db.sql

To run the tests

> python test_app.py

## Backend Reference

### Getting Started

- Base URL : This project is currently not hosted on a public domain, and can only be run locally. The default port used by the API is 5000, and the base URL is > http://localhost:5000/

- Authentication : Authentication is being done using Auth0.

### Error Handling

Errors are formatted in the JSON format, and an example of an error returned is show below:

    {
      "success" : False,
      "error" : 422,
      "message" : "Unprocessable"

    }
The following errors are handled by the API:

> - 400 : Bad Request
> - 404 : Resource Not Found
> - 405 : Method Not Allowed
> - 422 : Unprocessable
> - 401 : Unauthorized
> - 403 : Forbidden

### Endpoints

#### GET /categories

##### **Functionality provided**

> - Returns a list of all the categories from the database, which contains category name, description.


#### GET /categories/<category_id>/questions

##### **Functionality provided**

> - Returns a list of all the questions for the category passed in the url.
    
#### POST /categories/addcategory

##### **Functionality provided**

> - Creates a new category and posts it to the database.

#### POST /questions/<category_id>/addquestion

##### **Functionality provided**

> - Creates a new question for the given category and posts it to the database.

#### PATCH /questions/<int:question_id>/edit

##### **Functionality provided**

> - Edit any of the fields of a question like question title, question or answer.

#### DELETE /questions/<int:question_id>/delete

##### **Functionality provided**

> - Delete question from a particular category

# Authors

The entire web application was created by Siddharth Sampath.







