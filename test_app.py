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
        

        self.adminheader = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9aaUZONEhGOG9hMUNSVl96S1JldiJ9.eyJpc3MiOiJodHRwczovL2RhdGFyaXRobXMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMjNlZTEwMzJjZWEzMDIyMTE0MWEzNCIsImF1ZCI6ImRhdGFyaXRobXMiLCJpYXQiOjE1OTY5ODQzMTYsImV4cCI6MTU5NzA3MDcxNiwiYXpwIjoiWTV2TTBOdXZtN0hKN1UyUVJNdzVrT3RZZ3lqMmpGOEwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpxdWVzdGlvbiIsInBhdGNoOnF1ZXN0aW9uIiwicG9zdDpjYXRlZ29yeSIsInBvc3Q6cXVlc3Rpb24iXX0.PZLc_mnrJFdDWc8-HHNxzuKLcytAlqS5GZWVIRQ7uN0eG_Br4QfPB00ySUcUWo0IOHlXdnNlZdvgtDax9ButCgO1weyqTiS5XEn0ZnITgtHLIlV4cP34Zt7y3ya5EkqQUU01svR60qYuwiy8ZmsHTexzz9nRlITn2fgHFVxj72t8a7gNOgCujoD2shBZGwcYfYvMfBhjxxE6sdUfLuznuA8c3Nvmu0zQnD3tuwki3VTTrIJieuPuwrNWnPLuOwfiOiLBRpbnjPSbF-dON12C1GGFOn83WSsIBgO5wbFBVZtzMHdsxR3XheYqU5BWa_4HcQMD89CHNqOIs7LEDfP2aQ"
        self.editorheader = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9aaUZONEhGOG9hMUNSVl96S1JldiJ9.eyJpc3MiOiJodHRwczovL2RhdGFyaXRobXMudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmMzAyYjQ4N2VlMGYwMDAzZDhjYmUwOSIsImF1ZCI6ImRhdGFyaXRobXMiLCJpYXQiOjE1OTY5OTI2MTAsImV4cCI6MTU5NzA3OTAxMCwiYXpwIjoiWTV2TTBOdXZtN0hKN1UyUVJNdzVrT3RZZ3lqMmpGOEwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbInBhdGNoOnF1ZXN0aW9uIl19.iROjCE6Lq6hIySjMrls9htARcOafYxvkaPRUVazdTLi0dtqE3XHw4dsIs3E4OZ0vce5aUrCvn-3BFflA76jf2hCAwD7fBXeaTKCLNmyKMGiMhW0nx12UULuTNI0pEmZ6Nzhjsh7AsvzjLU9g3HUXDPPnnoPH5i9qOLZYDPU7rsnMZ61OEkq5D-9t8oy1w5qSSzqsAMFcCmhYR6Rg2sjDyUlg2ly8UeiVZkVr3MAaVOg6WLRZ1ByuC0yl_N1mf_DSmUTisj8Jfp1CCEyZtkxo2ht-nH4ul1oYV-RO_RQYpPUbDGpgAkPIW3tt7rRwJ-cwtHwwJDeESAbq0IkjCGKBJA"
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
        question_id = 9
        res = self.client().delete(f'/questions/{question_id}/delete',headers={"Authorization" : self.adminheader})
        # Checking for a 302, as after the post request, we are redirecting to the categories page on the frontend
        # The redirect function gives a response of 302
        self.assertEqual(res.status_code,302)
    
    def test_13_delete_question_unprocessable_error(self):
        question_id = 3000
        res = self.client().delete(f'/questions/{question_id}/delete',headers={"Authorization" : self.adminheader})
        self.assertEqual(res.status_code,400)
    
    def test_14_delete_question_auth_error(self):
        question_id = 11
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

