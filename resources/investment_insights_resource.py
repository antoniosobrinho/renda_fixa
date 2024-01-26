from flask_restful import Resource
from services.investment_simulation_service import InvestmentSimulationService
from repositories.investment_simulation_repository import InvestmentSimulationRepository

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
        
        service = InvestmentSimulationService(
            InvestmentSimulationRepository()
        )

        insights = service.get_simulations_insights()

        return insights, 200