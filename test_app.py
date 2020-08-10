from app import create_app
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setupdb
database_path = os.environ['TESTDATABASE_URL']
# from flask import session
from forms import CategoryForm,QuestionForm

class DataRithmsTestCase(unittest.TestCase):
    """This class represents the DataRithms test cases"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.app.config['SECRET_KEY'] = 'test_secret'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client
        setupdb(self.app, database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        

        self.adminheader = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9aaUZONEhGOG9hMUNSVl96S1JldiJ9.eyJpc3MiOiJodHRwczovL2RhdGFyaXRobXMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMjNlZTEwMzJjZWEzMDIyMTE0MWEzNCIsImF1ZCI6ImRhdGFyaXRobXMiLCJpYXQiOjE1OTcwNzcwNjgsImV4cCI6MTU5NzE2MzQ2OCwiYXpwIjoiWTV2TTBOdXZtN0hKN1UyUVJNdzVrT3RZZ3lqMmpGOEwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpxdWVzdGlvbiIsInBhdGNoOnF1ZXN0aW9uIiwicG9zdDpjYXRlZ29yeSIsInBvc3Q6cXVlc3Rpb24iXX0.bIEHWYY66GfsQWNDysBh-azlmQRcyJQzA-g-j_pKK-WGbcFcvWgoOakBtn2blUPUqkfH6lIH54m9aF2ARsuEJWOW3-IoUCXCqyyziTi1-grrHRkkVpvOxUwllOdQNaPURXll9_A-QE_025liCboU2jfAhh2wkXlW8_dC0LWYpAkIw3bNeLJoKOawfn9EKDDX-yXjBE7utPfylDxnHxiu3LWSXtMWZJlZnLUB_HYozdATNzspmsu99KA0QkhK9trhxZSBa_iPSIblLaNtvLJVhE9bO0Eyvq41dp_Q3NB-TntjGsAhvT-Nl9iTYRM63iu1K3G3MhP1LLbUzprJ0yX5vA"
        self.editorheader = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9aaUZONEhGOG9hMUNSVl96S1JldiJ9.eyJpc3MiOiJodHRwczovL2RhdGFyaXRobXMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzAyYjQ4N2VlMGYwMDAzZDhjYmUwOSIsImF1ZCI6ImRhdGFyaXRobXMiLCJpYXQiOjE1OTcwNzcxMzUsImV4cCI6MTU5NzE2MzUzNSwiYXpwIjoiWTV2TTBOdXZtN0hKN1UyUVJNdzVrT3RZZ3lqMmpGOEwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInBhdGNoOnF1ZXN0aW9uIl19.RQQbBOxx3xvUJkfk6PLYLqz1-ZGkTBcwuWM1iOMVd9LfPKtqFV_Anktwo8FFIPFic2t6onlokLycjcIRv7BEvZYoZRj-n1e-47x4xa4veQpPbs0v-EdKaeI8LEB7Pdy4ECyj1UqMcOw-XhA5FZn3zJGXGUBQIjHhPfg9n7Tu7_qxf4QIEiCbIrsfYfVt0ntDQTjPKRJPHB3QtP6F9sGElZRj7WszIAQz5eho7TEPQWuHT6X98DpfQL6jLBOilOxV_wE-KvZwvEF5dTbKW979vdlL4I7SphKh8j6x_2L8SZ5xzEZPY4X-JGPmyAuQ5N19lj2vK8cuWvsLZMgx6t59qg"
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    def test_1_setHeader(self):
        res = self.client().get('/setheader/', headers={"Authorization" : self.adminheader})
        self.assertEqual(res.status_code, 200)

    def test_2_landing_page(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_3_get_categories(self):
        res = self.client().get('/categories/')
        self.assertEqual(res.status_code, 200)
    
    def test_4_get_categories_error(self):
        res = self.client().get('/categories/1')
        self.assertEqual(res.status_code, 404)
    
    def test_5_create_category(self):
        res = self.client().post('/categories/addcategory/', 
                                     data={"category_name" : "New name",
                                         "category_description" : "asdad"}, headers={"Authorization" : self.adminheader})
        
        # Checking for a 302, as after the post request, we are redirecting to the categories page on the frontend
        # The redirect function gives a response of 302
        self.assertEqual(res.status_code, 302)
    
     
    def test_6_create_category_auth_error(self):
        res = self.client().post('/categories/addcategory/', 
                                     data={"category_name" : "New name",
                                         "category_description" : "asdad"})
        self.assertEqual(res.status_code, 401)
    
    def test_7_create_category_bad_request_error(self):
        res = self.client().post('/categories/addcategory/', headers={"Authorization" : self.adminheader})
        self.assertEqual(res.status_code, 422)

    def test_8_create_category_403_error(self):
        res = self.client().post('/categories/addcategory/', 
                                     data={"category_name" : "New name",
                                         "category_description" : "asdad"}, headers={"Authorization" : self.editorheader})
        
    def test_10_create_question(self):
        
        res = self.client().post('/categories/1/addquestion/', 
                                data={"question_title" : "New name",
                                      "question" : "asdad",
                                      "answer" : "answer"},headers={"Authorization" : self.adminheader})
        
        # Checking for a 302, as after the post request, we are redirecting to the categories page on the frontend
        # The redirect function gives a response of 302
        self.assertEqual(res.status_code, 302)

    def test_11_create_question_auth_error(self):
        
        res = self.client().post('/categories/1/addquestion/', 
                                data={"question_title" : "New name",
                                      "question" : "asdad",
                                      "answer" : "answer"})
        
        # Checking for a 302, as after the post request, we are redirecting to the categories page on the frontend
        # The redirect function gives a response of 302
        self.assertEqual(res.status_code, 401)   
    
    def test_12_delete_question(self):
        question_id = 12
        res = self.client().delete(f'/questions/{question_id}/delete',headers={"Authorization" : self.adminheader})
        # Checking for a 302, as after the post request, we are redirecting to the categories page on the frontend
        # The redirect function gives a response of 302
        self.assertEqual(res.status_code,302)
    
    def test_13_delete_question_unprocessable_error(self):
        question_id = 3000
        res = self.client().delete(f'/questions/{question_id}/delete',headers={"Authorization" : self.adminheader})
        self.assertEqual(res.status_code,400)
    
    def test_14_delete_question_auth_error(self):
        question_id = 14
        res = self.client().delete(f'/questions/{question_id}/delete')
        self.assertEqual(res.status_code,401)

    def test_15_edit_question(self):
        question_id = 6
        res = self.client().patch(f'/questions/{question_id}/edit', data={"question_title" : "New name",
                                      "question" : "asdad",
                                      "answer" : "answer"},headers={"Authorization" : self.editorheader})
        self.assertEqual(res.status_code,302)

    def test_16_edit_question_auth_error(self):
        question_id = 6
        res = self.client().patch(f'/questions/{question_id}/edit', data={"question_title" : "New name",
                                      "question" : "asdad",
                                      "answer" : "answer"})
        self.assertEqual(res.status_code,401)
    



if __name__ == "__main__":
    unittest.main()

