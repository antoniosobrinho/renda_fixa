from flask import Flask
from flask_restful import Api

#resources
from resources.investment_simulation_resource import InvestmentSimulationResource

app = Flask(__name__)
api = Api(app)

api.add_resource(InvestmentSimulationResource, '/investment_simulations')

app.run()
