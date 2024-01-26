from tests.setup_test import SetUpTest

class TestInvestmentInsightsResource(SetUpTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    #     for i in range(5):
    #         cls.create_investment_simulation()

    # def test_get_investment_insights(self):

    #     response = self.app.get('/investment_insights')
    #     self.assertEqual(response.status_code, 200)
    #     fields  = ['with_max_final_amount',
    #                 'with_min_final_amount',
    #                 'avg_final_amount',
    #                 'with_max_monthly_investment',
    #                 'with_min_monthly_investment']
        
    #     data = response.get_json()
    #     data_keys = data.keys()
    #     for field in fields:
    #         self.assertIn(field, data_keys)
