from app import create_app
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setupdb
database_path = os.environ['TESTDATABASE_URL']

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
    
    def test_sample(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()

