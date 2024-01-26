from models.investment_simulation import InvestmentSimulationModel
from i_investment_simulation_respository import InvestmentSimulationRepositoryInterface

class InvestmentSimulationRepository(InvestmentSimulationRepositoryInterface):

    def get_average_final_amount(self) -> float:
        
        average_final_amount = InvestmentSimulationModel.objects.average('final_amount')
        
        return average_final_amount

    def get_document_with_max_final_amount(self):

        with_max_amount = InvestmentSimulationModel.objects.order_by('-final_amount').first()

        return with_max_amount

    def get_document_with_min_final_amount(self):

        with_min_amount = InvestmentSimulationModel.objects.order_by('final_amount').first()

        return with_min_amount

    def get_document_with_max_monthly_investment(self):

        with_monthly_investment = InvestmentSimulationModel.objects.order_by('-monthly_investment').first()

        return with_monthly_investment

    
    def get_document_with_min_monthly_investment(self):

        with_monthly_investment = InvestmentSimulationModel.objects.order_by('monthly_investment').first()

        return with_monthly_investment

    def save(self, simulation:InvestmentSimulationModel) -> InvestmentSimulationModel:
        simulation.save()
        return simulation

    def create_simulation(self, data: dict) -> InvestmentSimulationModel:
        simulation = InvestmentSimulationModel(**data)
        simulation = self.save(simulation)
        return simulation