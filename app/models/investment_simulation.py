from mongoengine import (Document, StringField, IntField, 
                         FloatField, ValidationError)

class InvestmentSimulation(Document):

    COMPENSATION_CHOICES = ['post-fixed', 'pre-fixed']


    name = StringField(required=True, min_length=1)
    months_invested = IntField(required=True, min_value=1)
    initial_value = FloatField(required=True, min_value=0)
    monthly_investment = FloatField(required=True, min_value=0)
    monthly_interest_rate = FloatField(required=True, min_value=0)
    compensation = StringField(required=True)