from tests.setup_test import SetUpTest
from models.investment_simulation import InvestmentSimulationModel
from repositories.investment_simulation_repository import InvestmentSimulationRepository

class TestInvestmentSimulationRepository(SetUpTest):

    def setUp(self):
        self.simulation1 = InvestmentSimulationModel(
            name="Simulation 1",
            months_invested=12,
            initial_value=1000.0,
            monthly_investment=200.0,
            monthly_interest_rate=0.01,
            compensation="pre-fixed",
            final_amount=0.0
        )
        self.simulation1.save()

        self.simulation2 = InvestmentSimulationModel(
            name="Simulation 2",
            months_invested=24,
            initial_value=1500.0,
            monthly_investment=250.0,
            monthly_interest_rate=0.02,
            compensation="pre-fixed",
            final_amount=100000
        )
        self.simulation2.save()

        self.repository = InvestmentSimulationRepository()

    def tearDown(self):
        InvestmentSimulationModel.objects.delete()

    def test_get_average_final_amount(self):
        average_final_amount = self.repository.get_average_final_amount()
        self.assertEqual(average_final_amount, (self.simulation1.final_amount + self.simulation2.final_amount) / 2)

    def test_get_document_with_max_final_amount(self):
        document_with_max_amount = self.repository.get_document_with_max_final_amount()
        self.assertEqual(document_with_max_amount, self.simulation2)

    def test_get_document_with_min_final_amount(self):
        document_with_min_amount = self.repository.get_document_with_min_final_amount()
        self.assertEqual(document_with_min_amount, self.simulation1)

    def test_get_document_with_max_monthly_investment(self):
        document_with_max_monthly_investment = self.repository.get_document_with_max_monthly_investment()
        self.assertEqual(document_with_max_monthly_investment, self.simulation2)

    def test_get_document_with_min_monthly_investment(self):
        document_with_min_monthly_investment = self.repository.get_document_with_min_monthly_investment()
        self.assertEqual(document_with_min_monthly_investment, self.simulation1)

    def test_save(self):
        new_simulation = InvestmentSimulationModel(
            name="New Simulation",
            months_invested=6,
            initial_value=500.0,
            monthly_investment=100.0,
            monthly_interest_rate=0.015,
            compensation="pre-fixed",
            final_amount=0.0
        )
        saved_simulation = self.repository.save(new_simulation)
        self.assertIsNotNone(saved_simulation.id)

    def test_create_simulation(self):
        data = {
            "name": "Created Simulation",
            "months_invested": 18,
            "initial_value": 1200.0,
            "monthly_investment": 180.0,
            "monthly_interest_rate": 0.025,
            "compensation":"pre-fixed",
            "final_amount": 0.0
        }
        created_simulation = self.repository.create_simulation(data)
        self.assertIsNotNone(created_simulation.id)
        self.assertEqual(created_simulation.name, data["name"])
