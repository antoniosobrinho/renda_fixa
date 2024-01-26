from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from flasgger import swag_from
from schemas.investment_simulation_schema import InvestmentSimulationSchema
from services.investment_simulation_service import InvestmentSimulationService
from repositories.investment_simulation_repository import InvestmentSimulationRepository

class InvestmentSimulationResource(Resource):

    @swag_from('../swagger/investment_simulations/post.yml')
    def post(self):
        
        data = request.get_json() 
        simulation_schema = InvestmentSimulationSchema()
        try:
            simulation_schema.load(data)
        except ValidationError as e:
            return jsonify({"erro": str(e)}), 400

        simulation_service = InvestmentSimulationService(
            InvestmentSimulationRepository()
        )

        response_data = simulation_service.get_investment_values(data)
        
        return response_data, 201
    
