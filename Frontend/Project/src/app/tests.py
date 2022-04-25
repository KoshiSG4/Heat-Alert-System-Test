import unittest
from flask import Flask
from flask_mysqldb import MySQL,MySQLdb
# Bring your packages onto the path
# import sys, os
# sys.path.append('..')

# Now do your import
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

    # def test_bar_with_client(self,client):
    #     # Use the client here
    #     # Example login request (on a hypothetical app)
    #     rv = client.post('/login', {'username': 'koshi', 'password': 'secret_key'})
    #     # Make sure rv is a redirect request to index page
    #     self.assertLocationHeader('http://localhost/')
    #     # Make sure session is set
    #     self.assertIn('user_id', Flask.globals.session)				

if __name__ == "__main__":
    unittest.main()
