import unittest
from mongoengine import connect
from config import Config

class SetUpTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connect('test_database', host=Config.MONGODB_URI)
    