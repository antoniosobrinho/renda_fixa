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

        simulation = simulation_service.simulate_investment(data)
        
        total_invested = (simulation.initial_value + 
                          simulation.monthly_investment * 
                          simulation.months_invested)
        total_interest = round((simulation.final_amount - total_invested),2)

        response_data = {
            "final_amount": simulation.final_amount,
            "total_invested": total_invested,
            "total_interest": total_interest
        }

        return response_data, 201
    
