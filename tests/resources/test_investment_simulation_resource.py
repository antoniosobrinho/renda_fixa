from tests.setup_test import SetUpTest
from models.investment_simulation import InvestmentSimulationModel

class TestInvestmentSimulationResource(SetUpTest):

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        InvestmentSimulationModel.objects.delete()

    def test_post_valid_input(self):
        valid_data = {
            "name": "Test Simulation",
            "months_invested": 12,
            "initial_value": 1000.0,
            "monthly_investment": 200.0,
            "monthly_interest_rate": 1.0,
            "compensation": "post-fixed"
        }

        response = self.app.post('/investment_simulations', json=valid_data)

        self.assertEqual(response.status_code, 201)
        expected_response_data = {
            "final_amount": 3663.33,
            "total_invested": 3400.0,
            "total_interest": 263.33
        }
        self.assertEqual(response.get_json(), expected_response_data)

    def test_post_invalid_input(self):
        invalid_data = {
            "name": "",  
            "months_invested": 0,
            "initial_value": "invalid",
            "monthly_investment": -100.0,
            "monthly_interest_rate": "invalid",
            "compensation": "invalid"
        }

        response = self.app.post('/investment_simulations', json=invalid_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("name", response.data.decode('utf-8'))
        self.assertIn("months_invested", response.data.decode('utf-8'))
        self.assertIn("initial_value", response.data.decode('utf-8'))
        self.assertIn("monthly_investment", response.data.decode('utf-8'))
        self.assertIn("monthly_interest_rate", response.data.decode('utf-8'))
        self.assertIn("compensation", response.data.decode('utf-8'))
