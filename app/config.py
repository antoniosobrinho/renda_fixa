import os

class Config():
    DEBUG = False
    TESTING = False
    MONGODB_HOST = os.environ.get('MONGODB_HOST')
    DB = 'investment_database'
    MONGODB_URI = MONGODB_HOST + DB + '?authSource=admin'

class TestConfig(Config):
    TESTING = True
    DB = 'investment_database_test'
    MONGODB_URI = Config.MONGODB_HOST + DB + '?authSource=admin'