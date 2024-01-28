
from tests.setup_test import SetUpTest
from models.investment_simulation import InvestmentSimulationModel
import json

class TestInvestmentInsightsResource(SetUpTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.simulation1 = InvestmentSimulationModel(
            name="Simulation 1",
            months_invested=12,
            initial_value=1000.0,
            monthly_investment=200.0,
            monthly_interest_rate=0.01,
            compensation="pre-fixed",
            final_amount=0.0
        )
        cls.simulation1.save()

        cls.simulation2 = InvestmentSimulationModel(
            name="Simulation 2",
            months_invested=24,
            initial_value=1500.0,
            monthly_investment=250.0,
            monthly_interest_rate=0.02,
            compensation="pre-fixed",
            final_amount=100000
        )
        cls.simulation2.save()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        InvestmentSimulationModel.objects.delete()

    def test_get(self):
        fake_insights = {
            'with_max_final_amount': json.loads(self.simulation2.to_json()),
            'with_min_final_amount': json.loads(self.simulation1.to_json()),
            'avg_final_amount': (self.simulation1.final_amount + self.simulation2.final_amount) / 2,
            'with_max_monthly_investment': json.loads(self.simulation2.to_json()),
            'with_min_monthly_investment': json.loads(self.simulation1.to_json())
        }

        response = self.app.get('/investment_insights')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), fake_insights)
