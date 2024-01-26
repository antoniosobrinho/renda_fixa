from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from schemas.investment_simulation_schema import InvestmentSimulationSchema
from services.investment_simulation_service import InvestmentSimulationService
from repositories.investment_simulation_repository import InvestmentSimulationRepository

class InvestmentSimulationResource(Resource):

    def post(self):
        """
        Post an investment simulation
        ---
        parameters:
            -   name: name,
                in: query
                type: string
                required: true
                description: Name of the simulation
            -   name: months_invested,
                in: query
                type: integer
                required: true
                description: Time in months in which the money will be invested
            -   name: initial_value,
                in: query
                type: number
                required: true
                description: Initial value of the aplication
            -   name: monthly_investment,
                in: query
                type: number
                required: true
                description: Amount invested each month
            -   name: monthly_interest_rate,
                in: query
                type: number
                required: true
                description: Percentage earned each month
            -   name: compensation,
                in: query
                type: string
                enum: ["pre-fixed", "post-fixed"]
                required: true
                description: Name of the simulation
        responses:
            201:
                description: Simulation created
                schema:
                    properties:
                        final_amount:
                            type: number
                            description: Total value after months
                        total_invested:
                            type: number
                            description: Total value invested after months
                        total_interest:
                            type: number
                            description: Profit received
            400:
                description: Invalid request
        """

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
    
