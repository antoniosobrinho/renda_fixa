from flask import Flask
from flask_restful import Api
from mongoengine import connect
#resources
from resources.investment_simulation_resource import InvestmentSimulationResource
from resources.investment_insights_resource import InvestmentInsightsResource
from resources.health_check_resource import HealthCheckResource
#App
app = Flask(__name__)
api = Api(app)

app.config.from_object('config.Config')

connect(host=app.config['MONGODB_URI'])

#Endpoints
api.add_resource(InvestmentSimulationResource, '/investment_simulations')
api.add_resource(InvestmentInsightsResource, '/investment_insights')
api.add_resource(HealthCheckResource, '/health_check')