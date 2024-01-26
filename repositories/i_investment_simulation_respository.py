from abc import ABC, abstractmethod
from models.investment_simulation import InvestmentSimulation

class InvestmentSimulationRepositoryInterface(ABC):
    
    @abstractmethod
    def get_average_final_amount(self):
        pass

    @abstractmethod
    def get_document_with_max_final_amount(self):
        pass

    @abstractmethod
    def get_document_with_min_final_amount(self):
        pass

    @abstractmethod
    def get_document_with_max_monthly_investment(self):
        pass

    @abstractmethod
    def get_document_with_min_monthly_investment(self):
        pass

    @abstractmethod
    def save(self, simulation: InvestmentSimulation):
        pass

    @abstractmethod
    def create_simulation(self, data:dict):
        pass

