from abc import ABC, abstractmethod

class InvestmentSimulationServiceInterface(ABC):

    @abstractmethod
    def simulate_investment(self):
        pass
