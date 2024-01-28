import unittest
from unittest.mock import Mock
from models.investment_simulation import InvestmentSimulationModel
from services.investment_simulation_service import InvestmentSimulationService

class TestInvestmentSimulationService(unittest.TestCase):

    def setUp(self):
        self.repository_mock = Mock()
        self.service = InvestmentSimulationService(repository=self.repository_mock)

    def test_get_investment_values(self):
        investment_data = {
            'initial_value': 1000.0,
            'monthly_interest_rate': 1.5,
            'months_invested': 12,
            'monthly_investment': 200.0
        }

        simulated_investment = InvestmentSimulationModel(
            name="Test Simulation",
            months_invested=investment_data['months_invested'],
            initial_value=investment_data['initial_value'],
            monthly_investment=investment_data['monthly_investment'],
            monthly_interest_rate=investment_data['monthly_interest_rate'],
            compensation="pre-fixed",
            final_amount=1200.0 
        )

        self.repository_mock.create_simulation.return_value = simulated_investment

        result = self.service.get_investment_values(investment_data)

        expected_result = {
            'final_amount': 1200.0,
            'total_invested': 3400.0,  
            'total_interest': -2200.0
        }
        self.assertEqual(result, expected_result)

        self.repository_mock.create_simulation.assert_called_once_with(investment_data)

    def test_create_simulation(self):
        investment_data = {
            'initial_value': 1000.0,
            'monthly_interest_rate': 1.5,
            'months_invested': 12,
            'monthly_investment': 200.0
        }

        simulated_investment = InvestmentSimulationModel(
            name="Test Simulation",
            months_invested=investment_data['months_invested'],
            initial_value=investment_data['initial_value'],
            monthly_investment=investment_data['monthly_investment'],
            monthly_interest_rate=investment_data['monthly_interest_rate'],
            compensation="compensation_type",
            final_amount=1200.0  
        )

        self.repository_mock.create_simulation.return_value = simulated_investment

        result = self.service._InvestmentSimulationService__create_simulate_investment(investment_data)

        self.assertEqual(result, simulated_investment)

        self.repository_mock.create_simulation.assert_called_once_with(investment_data)
