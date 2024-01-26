import os

class Config():
    DEBUG = False
    TESTING = False
    MONGODB_HOST = os.environ.get('MONGODB_HOST', 'mongodb://root:root@localhost:27017/')
    DB = 'investment_database'
    MONGODB_URI = MONGODB_HOST + DB + '?authSource=admin'
