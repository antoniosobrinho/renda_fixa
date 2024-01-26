from flask_restful import Resource
from flasgger import swag_from
from services.investment_insights_service import InvestmentInsightsService
from repositories.investment_simulation_repository import InvestmentSimulationRepository

class InvestmentInsightsResource(Resource):

    @swag_from('../swagger/investment_insights/get.yml')
    def get(self):
               
        service = InvestmentInsightsService(
            InvestmentSimulationRepository()
        )

        insights = service.get_simulations_insights()

        return insights, 200