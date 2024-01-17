from flask_restful import Resource
from flask import request
from schemas.investment_simulation_schema import InvestmentSimulationSchema
from models.investment_simulation import InvestmentSimulation
from utils.investment_utils import InvestmentUtils

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
        if not data:
            return {'error': 'Invalid JSON format'}, 400

        simulation_schema = InvestmentSimulationSchema()
        errors = simulation_schema.validate(data)

        if errors:
            return {'error': 'Validation error', 'message': errors}, 400

        initial_value = data['initial_value']
        monthly_interest_rate = data['monthly_interest_rate']
        months_invested = data['months_invested']
        monthly_investment = data['monthly_investment']

        #percent
        monthly_interest_rate = monthly_interest_rate/100
        
        investment_utils = InvestmentUtils()

        final_amount = investment_utils.calculate_compound_interest(
            initial_value, monthly_interest_rate, 
            months_invested, monthly_investment
        )
        
        total_invested = initial_value + monthly_investment * months_invested

        total_interest = round((final_amount - total_invested),2)

        response_data = {
            "final_amount": final_amount,
            "total_invested": total_invested,
            "total_interest": total_interest
        }

        investment_simulation = InvestmentSimulation(**data, final_amount=final_amount)
        investment_simulation.save()

        return response_data, 201
    
