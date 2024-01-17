import unittest
from mongomock import MongoClient
from app import app
from models.investment_simulation import InvestmentSimulation
from utils.investment_utils import InvestmentUtils
from random import randint, random

class SetUpTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.testing = True
        cls.app = app.test_client()
        cls.mongo_client = MongoClient()
        cls.mongo_db = cls.mongo_client['test_database']

    @classmethod
    def tearDownClas(cls):
        cls.mongo_client.close()

    @classmethod
    def create_investment_simulation(cls):

        data = {
            "name": "new investment",
            "months_invested": randint(1, 12),
            "initial_value": random() * 10000,
            "monthly_investment": random() * 10000,
            "monthly_interest_rate": random(),
            "compensation": "pre-fixed"
        }

        utils = InvestmentUtils()

        data['final_amount'] = utils.calculate_compound_interest(
            data['initial_value'], data['monthly_interest_rate'], 
            data['months_invested'], data['monthly_investment']
        )
        
        simulation = InvestmentSimulation(**data)

        simulation.save()

        return simulation