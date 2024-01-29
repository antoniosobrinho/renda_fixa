from abc import ABC, abstractmethod

class InvestmentInsightsServiceInterface(ABC):
  
    @abstractmethod
    def get_simulations_insights(self):
        pass