from marshmallow import Schema, fields, validate

class InvestmentSimulationSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    months_invested = fields.Int(required=True, validate=validate.Range(min=1))
    initial_value = fields.Float(required=True, validate=validate.Range(min=0))
    monthly_investment = fields.Float(required=True, validate=validate.Range(min=0))
    monthly_interest_rate = fields.Float(required=True, validate=validate.Range(min=0))
    compensation = fields.Str(required=True, validate=validate.OneOf(['post-fixed', 'pre-fixed']))