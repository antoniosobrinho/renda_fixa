from flask_restful import Resource
from models.investment_simulation import InvestmentSimulation
from bson import json_util
import json

class InvestmentInsightsResource(Resource):

    def get(self):
        """
        Get an investment insights
        ---
        responses:
            200:
                description: Investment insights
                schema:
                    properties:
                        with_max_final_amount:
                            type: number
                            description: simulation with maximum final amount
                        with_min_final_amount:
                            type: number
                            description: simulation with minimum final amount
                        avg_final_amount:
                            type: number
                            description: avarege final amount of all simulations
                        with_max_monthly_investment:
                            type: number
                            description: simulation with maximum monthly investment
                        with_min_monthly_investment:
                            type: number
                            description: simulation with minimum monthly investment

        """
        with_max_final_amount = InvestmentSimulation.get_document_with_max_final_amount().to_json()
        with_min_final_amount = InvestmentSimulation.get_document_with_min_final_amount().to_json()
        avg_final_amount = InvestmentSimulation.get_average_final_amount()
        with_max_monthly_investment = InvestmentSimulation.get_document_with_max_monthly_investment().to_json()
        with_min_monthly_investment = InvestmentSimulation.get_document_with_min_monthly_investment().to_json()

        return {
            'with_max_final_amount' : json.loads(with_max_final_amount),
            'with_min_final_amount' : json.loads(with_min_final_amount),
            'avg_final_amount' : avg_final_amount,
            'with_max_monthly_investment' : json.loads(with_max_monthly_investment),
            'with_min_monthly_investment' : json.loads(with_min_monthly_investment)
            }, 200