from marshmallow import Schema, validate
from schemas.custom_fields import FloatField

class InvestmentSimulationResponseSchema(Schema):
    final_amount = FloatField(required=True, validate=validate.Range(min=0))
    total_invested = FloatField(required=True, validate=validate.Range(min=0))
    total_interest = FloatField(required=True, validate=validate.Range(min=0))
