import mongoengine

class InvestmentSimulationModel(mongoengine.Document):

    name = mongoengine.StringField(required=True, min_length=1)
    months_invested = mongoengine.IntField(required=True, min_value=1)
    initial_value = mongoengine.FloatField(required=True, min_value=0)
    monthly_investment = mongoengine.FloatField(required=True, min_value=0)
    monthly_interest_rate = mongoengine.FloatField(required=True, min_value=0)
    compensation = mongoengine.StringField(required=True)
    final_amount = mongoengine.FloatField(required=True, min_value=0)
