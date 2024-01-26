from tests.setup_test import SetUpTest
import copy

class TestInvestmentSimulationResource(SetUpTest):
    
    # def test_post_simulation(self):

    #     compensation_choices = ['post-fixed', 'pre-fixed']

    #     for compensation in compensation_choices:
    #         data = {
    #             "name": "new investment",
    #             "months_invested": 12,
    #             "initial_value": 5500,
    #             "monthly_investment": 4000,
    #             "monthly_interest_rate": 1,
    #             "compensation": compensation
    #         }

    #         response = self.app.post('/investment_simulations', json=data)
    #         self.assertEqual(response.status_code, 201)

    #     response_data = response.get_json()

    #     investment_utils = InvestmentUtils()
        
    #     final_amount = investment_utils.calculate_compound_interest(
    #         data['initial_value'], data['monthly_interest_rate']/100, 
    #         data['months_invested'], data['monthly_investment']
    #     )

    #     total_invested = data['initial_value'] + data['monthly_investment'] * data['months_invested']

    #     total_interest = round((final_amount - total_invested),2)

    #     self.assertEqual(response_data['final_amount'], final_amount)
    #     self.assertEqual(response_data['total_invested'], total_invested)
    #     self.assertEqual(response_data['total_interest'], total_interest)

    def test_post_simulation_without_required_field(self):

        data = {
            "name": "new investment",
            "months_invested": 12,
            "initial_value": 5500,
            "monthly_investment": 4000,
            "monthly_interest_rate": 1,
            "compensation": "pre-fixed"
        }

        for key in data.keys():
            data_without_field = copy.copy(data)
            del data_without_field[key]
            response = self.app.post('/investment_simulations', json=data_without_field)
            self.assertEqual(response.status_code, 400)
        

    def test_post_simulation_with_no_string_name(self):

        data = {
            "name": 2,
            "months_invested": 12,
            "initial_value": 5500,
            "monthly_investment": 4000,
            "monthly_interest_rate": 1,
            "compensation": "pre-fixed"
        }
       
        response = self.app.post('/investment_simulations', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_simulation_with_no_int_months_invested(self):

        data = {
            "name": "new simulation",
            "months_invested": "a",
            "initial_value": 5500,
            "monthly_investment": 4000,
            "monthly_interest_rate": 1,
            "compensation": "pre-fixed"
        }
       
        response = self.app.post('/investment_simulations', json=data)
        self.assertEqual(response.status_code, 400)
    
    def test_post_simulation_with_no_float_initial_value(self):

        data = {
            "name": "new investment",
            "months_invested": 12,
            "initial_value": "a",
            "monthly_investment": 4000,
            "monthly_interest_rate": 1,
            "compensation": "pre-fixed"
        }

        response = self.app.post('/investment_simulations', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_simulation_with_no_float_monthly_investment(self):

        data = {
            "name": "new investment",
            "months_invested": 12,
            "initial_value": 5500,
            "monthly_investment": "a",
            "monthly_interest_rate": 1,
            "compensation": "pre-fixed"
        }

        response = self.app.post('/investment_simulations', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_simulation_with_no_float_monthly_interest_rate(self):

        data = {
            "name": "new investment",
            "months_invested": 12,
            "initial_value": 5500,
            "monthly_investment": 4000,
            "monthly_interest_rate": "a",
            "compensation": "pre-fixed"
        }

        response = self.app.post('/investment_simulations', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_simulation_with_no_valid_compensation(self):

        data = {
            "name": "new investment",
            "months_invested": 12,
            "initial_value": 5500,
            "monthly_investment": 4000,
            "monthly_interest_rate": "a",
            "compensation": "stock"
        }

        response = self.app.post('/investment_simulations', json=data)
        self.assertEqual(response.status_code, 400)