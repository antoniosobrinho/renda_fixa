from abc import ABC, abstractmethod
from models.investment_simulation import InvestmentSimulationModel

class InvestmentSimulationRepositoryInterface(ABC):
    
    @abstractmethod
    def get_average_final_amount(self) -> float:
        pass

    @abstractmethod
    def get_document_with_max_final_amount(self) -> InvestmentSimulationModel:
        pass

    @abstractmethod
    def get_document_with_min_final_amount(self) -> InvestmentSimulationModel:
        pass

    @abstractmethod
    def get_document_with_max_monthly_investment(self) -> InvestmentSimulationModel:
        pass

    @abstractmethod
    def get_document_with_min_monthly_investment(self) -> InvestmentSimulationModel:
        pass

    @abstractmethod
    def save(self, simulation: InvestmentSimulationModel) -> InvestmentSimulationModel:
        pass

    @abstractmethod
    def create_simulation(self, data:dict) -> InvestmentSimulationModel:
        pass

