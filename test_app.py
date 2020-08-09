from app import create_app
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setupdb
database_path = os.environ['TESTDATABASE_URL']
from flask import session
from forms import CategoryForm,QuestionForm

class DataRithmsTestCase(unittest.TestCase):
    """This class represents the DataRithms test cases"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setupdb(self.app, database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    def test_setHeader(self, headers={"Authorization" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9aaUZONEhGOG9hMUNSVl96S1JldiJ9.eyJpc3MiOiJodHRwczovL2RhdGFyaXRobXMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMjNlZTEwMzJjZWEzMDIyMTE0MWEzNCIsImF1ZCI6ImRhdGFyaXRobXMiLCJpYXQiOjE1OTY5MDY0NzUsImV4cCI6MTU5Njk5Mjg3NSwiYXpwIjoiWTV2TTBOdXZtN0hKN1UyUVJNdzVrT3RZZ3lqMmpGOEwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpxdWVzdGlvbiIsInBhdGNoOnF1ZXN0aW9uIiwicG9zdDpjYXRlZ29yeSIsInBvc3Q6cXVlc3Rpb24iXX0.FdR_a8TMlPTyJFqhSaM1dWv2ILLCRfrG2dq408JajcAFQlTKxeQaEM3buvqtkiXpOULxYd5R5DuA0BWDFgTD346uo4Fcsk0Nuknzw8IeUfqkwcPAqbxghq3BsEARyjtZikRoCMlWs-OcFDo1i0OXDBtSV2DlkarQnNk6YyywJdfWqqKn0dMSAyjtX-Qk5i1aSwZjoOTlYMai9tbgfuJ81EJg_wYOxo-ag-QP_tiNRKEWJQpxIHairF3_QZXSmAQqttV-ciyBgNdTc0CjWVIiXDLjE7jllPwOORmdod841_xlBefCmT79sLQXmt6S82o4WXdWss9tUXTqzYt_KJubnA"}):
        res = self.client().get('/setheader/')
        self.assertEqual(res.status_code, 200)

    def test_landing_page(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_get_categories(self):
        res = self.client().get('/categories/')
        self.assertEqual(res.status_code, 200)
    
    def test_get_categories_error(self):
        res = self.client().get('/categories/1')
        self.assertEqual(res.status_code, 404)
    
    def test_create_category(self):
        res = self.client().post('/categories/addcategory/', 
                                data={"category_name" : "New name",
                                      "category_description" : "asdad"})
        self.assertEqual(res.status_code, 200)

    def test_create_question(self):
        res = self.client().post('/categories/1/addquestion/', 
                                data={"question_title" : "New name",
                                      "question" : "asdad",
                                      "answer" : "answer"})
        self.assertEqual(res.status_code, 200)   
        
        # self.assertEqual(res_data["code"], "invalid_header")
        

if __name__ == "__main__":
    unittest.main()

