from abc import ABC, abstractmethod

class InvestmentSimulationServiceInterface(ABC):
  
    @abstractmethod
    def get_investment_values(self, investment_data:dict) -> dict:
        pass
