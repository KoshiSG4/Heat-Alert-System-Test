import unittest
from flask import Flask
from flask_mysqldb import MySQL,MySQLdb

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

    def test_customer_count(self):
        self.assertEqual(len(self.app.temp), 10)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id='2018-06-19')
        self.assertEqual(customer.open,"50")
        self.assertEqual(customer.volume, "13439267")


class TestComplexData(unittest.TestCase):
    def setUp(self):
        # load test data
        self.app = open('Frontend/Project/src/app/data.json').read()

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 20)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id='2018-05-25')
        self.assertEqual(customer.open,"98.3000")
        self.assertEqual(customer.volume, "18363918")	

if __name__ == "__main__":
    unittest.main()
