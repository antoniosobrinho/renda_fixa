import unittest
from unittest.mock import Mock
from models.investment_simulation import InvestmentSimulationModel
from services.investment_insights_service import InvestmentInsightsService

class TestInvestmentInsightsService(unittest.TestCase):

    def setUp(self):
        self.repository_mock = Mock()

        self.service = InvestmentInsightsService(repository=self.repository_mock)

    def test_get_simulations_insights(self):
        mock_with_max_final_amount = InvestmentSimulationModel(
            name="Simulation with Max Final Amount",
            months_invested=12,
            initial_value=1000.0,
            monthly_investment=200.0,
            monthly_interest_rate=0.01,
            compensation="pre-fixed",
            final_amount=1500.0
        )
        mock_with_min_final_amount = InvestmentSimulationModel(
            name="Simulation with Min Final Amount",
            months_invested=12,
            initial_value=1000.0,
            monthly_investment=200.0,
            monthly_interest_rate=0.01,
            compensation="pre-fixed",
            final_amount=800.0
        )
        mock_with_max_monthly_investment = InvestmentSimulationModel(
            name="Simulation with Max Monthly Investment",
            months_invested=12,
            initial_value=1000.0,
            monthly_investment=250.0,
            monthly_interest_rate=0.01,
            compensation="pre-fixed",
            final_amount=1200.0
        )
        mock_with_min_monthly_investment = InvestmentSimulationModel(
            name="Simulation with Min Monthly Investment",
            months_invested=12,
            initial_value=1000.0,
            monthly_investment=180.0,
            monthly_interest_rate=0.01,
            compensation="pre-fixed",
            final_amount=1000.0
        )

        self.repository_mock.get_document_with_max_final_amount.return_value = mock_with_max_final_amount
        self.repository_mock.get_document_with_min_final_amount.return_value = mock_with_min_final_amount
        self.repository_mock.get_average_final_amount.return_value = 1100.0
        self.repository_mock.get_document_with_max_monthly_investment.return_value = mock_with_max_monthly_investment
        self.repository_mock.get_document_with_min_monthly_investment.return_value = mock_with_min_monthly_investment

        result = self.service.get_simulations_insights()

        expected_result = {
            'with_max_final_amount': {
                'name': 'Simulation with Max Final Amount',
                'months_invested': 12,
                'initial_value': 1000.0,
                'monthly_investment': 200.0,
                'monthly_interest_rate': 0.01,
                'compensation': 'pre-fixed',
                'final_amount': 1500.0
            },
            'with_min_final_amount': {
                'name': 'Simulation with Min Final Amount',
                'months_invested': 12,
                'initial_value': 1000.0,
                'monthly_investment': 200.0,
                'monthly_interest_rate': 0.01,
                'compensation': 'pre-fixed',
                'final_amount': 800.0
            },
            'avg_final_amount': 1100.0,
            'with_max_monthly_investment': {
                'name': 'Simulation with Max Monthly Investment',
                'months_invested': 12,
                'initial_value': 1000.0,
                'monthly_investment': 250.0,
                'monthly_interest_rate': 0.01,
                'compensation': 'pre-fixed',
                'final_amount': 1200.0
            },
            'with_min_monthly_investment': {
                'name': 'Simulation with Min Monthly Investment',
                'months_invested': 12,
                'initial_value': 1000.0,
                'monthly_investment': 180.0,
                'monthly_interest_rate': 0.01,
                'compensation': 'pre-fixed',
                'final_amount': 1000.0
            }
        }
        self.assertEqual(result, expected_result)

        self.repository_mock.get_document_with_max_final_amount.assert_called_once()
        self.repository_mock.get_document_with_min_final_amount.assert_called_once()
        self.repository_mock.get_average_final_amount.assert_called_once()
        self.repository_mock.get_document_with_max_monthly_investment.assert_called_once()
        self.repository_mock.get_document_with_min_monthly_investment.assert_called_once()