from pymongo import MongoClient
import os

mongo_uri = os.environ.get('MONGO_URI', 'mongodb://root:root@mongo:27017/investment_database?authSource=admin')
client = MongoClient(mongo_uri)
db = client.get_default_database()