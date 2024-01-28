import unittest
from unittest.mock import patch
from flask import Flask
from validation_decorator.validation_simulation_investment import validate_investment_simulation_data

class TestDecorator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.app = Flask(__name__)

        @cls.app.route('/fake-endpoint', methods=['POST'])
        @validate_investment_simulation_data()
        def fake_endpoint():
            return "Valid data received"


    def test_validate_investment_simulation_data_valid_input(self):
        valid_data = {
            "name": "Test Simulation",
            "months_invested": 12,
            "initial_value": 1000.0,
            "monthly_investment": 200.0,
            "monthly_interest_rate": 0.01,
            "compensation": "post-fixed"
        }

        response = self.app.test_client().post('/fake-endpoint', json=valid_data)

        self.assertEqual(response.data.decode('utf-8'), "Valid data received")

    #name
    def test_empty_name(self):
        invalid_data = {"name": "", 
                        "months_invested": 1, 
                        "initial_value": 1000.0,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}
        
        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.data.decode('utf-8'))

    def test_no_string_name(self):
        invalid_data = {"name": 1, 
                        "months_invested": 1, 
                        "initial_value": 1000.0,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.data.decode('utf-8'))
    
    #months_invested
    def test_zero_months_invested(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 0, 
                        "initial_value": 1000.0,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("months_invested", response.data.decode('utf-8'))
    
    def test_negative_months_invested(self):
        invalid_data = {"name": "Test", 
                        "months_invested": -12, 
                        "initial_value": 1000.0,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}


        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("months_invested", response.data.decode('utf-8'))
    
    def test_float_months_invested(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 0.5, 
                        "initial_value": 1000.0,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}


        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("months_invested", response.data.decode('utf-8'))

    def test_string_months_invested(self):
        invalid_data = {"name": "Test", 
                        "months_invested": "0", 
                        "initial_value": 1000.0,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}


        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("months_invested", response.data.decode('utf-8'))
    
    #initial_value
    def test_negative_initial_value(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": -10000.0,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("initial_value", response.data.decode('utf-8'))
    
    def test_integer_initial_value(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 1,
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}


        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("initial_value", response.data.decode('utf-8'))
    
    def test_string_initial_value(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": "0.0",
                        "monthly_investment": 200.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}


        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("initial_value", response.data.decode('utf-8'))
    
    #monthly_investment
    def test_negative_monthly_investment(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 10000.0,
                        "monthly_investment": -10000.0, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("monthly_investment", response.data.decode('utf-8'))

    def test_integer_monthly_investment(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 10000.0,
                        "monthly_investment": 1, 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}


        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("monthly_investment", response.data.decode('utf-8'))
    
    def test_string_monthly_investment(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 10000.0,
                        "monthly_investment": "1", 
                        "monthly_interest_rate": 0.01, 
                        "compensation": "post-fixed"}


        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("monthly_investment", response.data.decode('utf-8'))

    #monthly_interest_rate
    def test_negative_monthly_interest_rate(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 10000.0,
                        "monthly_investment": 10000.0, 
                        "monthly_interest_rate": -0.01, 
                        "compensation": "post-fixed"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("monthly_interest_rate", response.data.decode('utf-8'))

    def test_integer_monthly_interest_rate(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 10000.0,
                        "monthly_investment": 10000.0, 
                        "monthly_interest_rate": -1, 
                        "compensation": "post-fixed"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("monthly_interest_rate", response.data.decode('utf-8'))
    
    def test_string_monthly_interest_rate(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 10000.0,
                        "monthly_investment": 10000.0, 
                        "monthly_interest_rate": "0.01", 
                        "compensation": "post-fixed"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("monthly_interest_rate", response.data.decode('utf-8'))

    #compensation
    def test_invalid_compensation(self):
        invalid_data = {"name": "Test", 
                        "months_invested": 1, 
                        "initial_value": 10000.0,
                        "monthly_investment": 10000.0, 
                        "monthly_interest_rate": -0.01, 
                        "compensation": "compensation"}

        response = self.app.test_client().post('/fake-endpoint', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("compensation", response.data.decode('utf-8'))