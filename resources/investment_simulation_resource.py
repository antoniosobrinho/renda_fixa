from flask_restful import Resource
from flask import request
from flasgger import swag_from
from services.investment_simulation_service import InvestmentSimulationService
from repositories.investment_simulation_repository import InvestmentSimulationRepository
from validation_decorator.validation_simulation_investment import json_required, validate_investment_simulation_data
from schemas.investment_simulation_response_schema import InvestmentSimulationResponseSchema

class InvestmentSimulationResource(Resource):

    @swag_from('../swagger/investment_simulations/post.yml')
    @json_required()
    @validate_investment_simulation_data()
    def post(self):
        
        data = request.get_json() 
        
        simulation_service = InvestmentSimulationService(
            InvestmentSimulationRepository()
        )

        investment_values = simulation_service.get_investment_values(data)
        response_schema = InvestmentSimulationResponseSchema().dump(investment_values)

        return response_schema, 201
    
