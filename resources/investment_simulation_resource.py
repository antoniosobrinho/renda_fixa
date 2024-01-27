from flask_restful import Resource
from flask import request
from flasgger import swag_from
from services.investment_simulation_service import InvestmentSimulationService
from repositories.investment_simulation_repository import InvestmentSimulationRepository
from validation_decorator.validation_simulation_investment import json_required, validate_investment_simulation_data
class InvestmentSimulationResource(Resource):

    @swag_from('../swagger/investment_simulations/post.yml')
    @json_required()
    @validate_investment_simulation_data()
    def post(self):
        
        data = request.get_json() 
        
        simulation_service = InvestmentSimulationService(
            InvestmentSimulationRepository()
        )

        response_data = simulation_service.get_investment_values(data)
        
        return response_data, 201
    
