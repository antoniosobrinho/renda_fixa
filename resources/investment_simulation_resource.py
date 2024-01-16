from flask_restful import Resource
from flask import request
from db.config import db
from schemas.investment_simulation_schema import InvestmentSimulationSchema
investment_simulation_collection = db['investment_simulations']

class InvestmentSimulationResource(Resource):

    def post(self):

        data = request.get_json() 
        if not data:
            return {'error': 'Invalid JSON format'}, 400

        simulation_schema = InvestmentSimulationSchema()
        errors = simulation_schema.validate(data)

        if errors:
            return {'error': 'Validation error', 'message': errors}, 400

        
        # investment_simulation_id = investment_simulation_collection.insert_one(
        #                                                             {'data': json_data}
        #                                                         ).inserted_id

        # return {str(investment_simulation_id): json_data}
    
