from repositories.i_investment_simulation_respository import InvestmentSimulationRepositoryInterface
from models.investment_simulation import InvestmentSimulationModel
from services.i_investment_simulation_service import InvestmentSimulationServiceInterface
import json

class InvestmentSimulationService(InvestmentSimulationServiceInterface):

    def __init__(self, repository: InvestmentSimulationRepositoryInterface) -> None:
        self.repository = repository
    
    def get_investment_values(self, investment_data:dict) -> dict:
        
        simulation = self.__create_simulate_investment(investment_data)

        total_invested = (simulation.initial_value + 
                          simulation.monthly_investment * 
                          simulation.months_invested)
        total_interest = round((simulation.final_amount - total_invested),2)

        investment_values = {
            "final_amount": simulation.final_amount,
            "total_invested": total_invested,
            "total_interest": total_interest
        }

        return investment_values
        
    def __create_simulate_investment(self, investment_data:dict) -> InvestmentSimulationModel:

        initial_value = investment_data['initial_value']
        monthly_interest_rate = investment_data['monthly_interest_rate']
        months_invested = investment_data['months_invested']
        monthly_investment = investment_data['monthly_investment']

        #percent
        monthly_interest_rate = monthly_interest_rate/100
        
        final_amount = self.__calculate_compound_interest(
            initial_value, monthly_interest_rate, 
            months_invested, monthly_investment
        )

        investment_data['final_amount'] = final_amount

        simulation = self.repository.create_simulation(investment_data)

        return simulation
    
    def __calculate_compound_interest(
            self, 
            initial_value:float, 
            interest_rate:float, 
            period:int, 
            periodic_application:float=0) -> float:
        
        final_amount = (initial_value * ((1 + interest_rate)**period)  
                        + periodic_application * (
                                ((1 + interest_rate)**period - 1) / interest_rate
                            )
                        )
        
        return round(final_amount,2)
    
