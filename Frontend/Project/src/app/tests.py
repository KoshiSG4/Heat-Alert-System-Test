import unittest
from flask import Flask
from flask_mysqldb import MySQL,MySQLdb

import app

    
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

    def test_dataset_count(self):
        self.assertEqual(len(self.app.Information), 10)

    def test_existence_of_customer(self):
        Time_Series = self.app.get_Information(id='2018-06-19')
        self.assertEqual(Time_Series.open,"50")
        self.assertEqual(Time_Series.volume, "13439267")



if __name__ == "__main__":
    unittest.main()
