from flask import Flask
from flask_restful import Api
from mongoengine import connect
#resources
from resources.investment_simulation_resource import InvestmentSimulationResource
from resources.investment_insights_resource import InvestmentInsightsResource

#App
app = Flask(__name__)
api = Api(app)

app.config.from_object('config.Config')

connect(host=app.config['MONGODB_HOST'])

#Endpoints
api.add_resource(InvestmentSimulationResource, '/investment_simulations')
api.add_resource(InvestmentInsightsResource, '/investment_insights')