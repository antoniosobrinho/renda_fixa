from marshmallow import Schema, fields, validate
from schemas.custom_fields import IntegerField, FloatField
from schemas.errors_i18n import error_messages

class InvestmentSimulationSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1), error_messages=error_messages)
    months_invested = IntegerField(required=True, validate=validate.Range(min=1), error_messages=error_messages)
    initial_value = FloatField(required=True, validate=validate.Range(min=0), error_messages=error_messages)
    monthly_investment = FloatField(required=True, validate=validate.Range(min=0), error_messages=error_messages)
    monthly_interest_rate = FloatField(required=True, validate=validate.Range(min=0), error_messages=error_messages)
    compensation = fields.Str(required=True, validate=validate.OneOf(['post-fixed', 'pre-fixed']), error_messages=error_messages)
