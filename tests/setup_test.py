import unittest
from mongoengine import connect
from config import Config
from app import app

class SetUpTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('test_database', host=Config.MONGODB_URI)
        app.testing = True
        cls.app = app.test_client()
    