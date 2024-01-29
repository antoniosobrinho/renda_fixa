from repositories.interfaces.i_investment_simulation_respository import InvestmentSimulationRepositoryInterface
from services.interfaces.i_investment_insights_service import InvestmentInsightsServiceInterface
import json

class InvestmentInsightsService(InvestmentInsightsServiceInterface):

    def __init__(self, repository: InvestmentSimulationRepositoryInterface) -> None:
        self.repository = repository
    
    def get_simulations_insights(self) -> dict:
        
        with_max_final_amount = self.repository.get_document_with_max_final_amount().to_json()
        with_min_final_amount = self.repository.get_document_with_min_final_amount().to_json()
        avg_final_amount = self.repository.get_average_final_amount()
        with_max_monthly_investment = self.repository.get_document_with_max_monthly_investment().to_json()
        with_min_monthly_investment = self.repository.get_document_with_min_monthly_investment().to_json()

        
        return {
            'with_max_final_amount' : json.loads(with_max_final_amount),
            'with_min_final_amount' : json.loads(with_min_final_amount),
            'avg_final_amount' : avg_final_amount,
            'with_max_monthly_investment' : json.loads(with_max_monthly_investment),
            'with_min_monthly_investment' : json.loads(with_min_monthly_investment)
            }
    
