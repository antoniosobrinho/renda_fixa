from marshmallow import Schema, fields, validate
from schemas.custom_fields import IntegerField, FloatField

class InvestmentSimulationSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    months_invested = IntegerField(required=True, validate=validate.Range(min=1))
    initial_value = FloatField(required=True, validate=validate.Range(min=0))
    monthly_investment = FloatField(required=True, validate=validate.Range(min=0))
    monthly_interest_rate = FloatField(required=True, validate=validate.Range(min=0))
    compensation = fields.Str(required=True, validate=validate.OneOf(['post-fixed', 'pre-fixed']))
