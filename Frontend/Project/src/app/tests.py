import unittest
from flask import Flask
from flask_mysqldb import MySQL,MySQLdb
from pathlib import Path

THIS_DIR = Path(__file__).parent

my_data_path = THIS_DIR.parent / 'Frontend/Project/src/app/app.py'

from app import app

    
class TestRestApi(unittest.TestCase):
    #check if response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    #check if content return is charset=utf-8
    def test_index_context(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type,"text/html; charset=utf-8")

    # check for data returned 
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue(b'date' in response.data)
        self.assertTrue(b'panel_id' in response.data)
        self.assertTrue(b'DC_Power' in response.data)
        self.assertTrue(b'AC_Power' in response.data)
        self.assertTrue(b'daily_yeild' in response.data)
        self.assertTrue(b'total_yeild' in response.data)
        self.assertTrue(b'ambient_temperature' in response.data)
        self.assertTrue(b'module_temperature' in response.data)
        self.assertTrue(b'irrediance' in response.data)	

class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = open('Frontend/Project/src/app/data.json').read()
        
    def test_data(self):
        tester = app.test_client(self)
        response = tester.get('2018-06-19')
        self.assertTrue(b'50' in response.data)

    



if __name__ == "__main__":
    unittest.main()
