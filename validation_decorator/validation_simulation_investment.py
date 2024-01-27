from flask import abort, request
from functools import wraps
from schemas.investment_simulation_schema import InvestmentSimulationSchema

def json_required():

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not request.is_json:
                abort(400, 'Request content must be a valid json')

            return fn(*args, **kwargs)
        return wrapper
    return decorator

def validate_investment_simulation_data():

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            data = request.get_json()
           
            simulation_schema = InvestmentSimulationSchema()
        
            errors = simulation_schema.validate(data)
            if errors:
                abort(400, errors)

            return fn(*args, **kwargs)
        return wrapper
    return decorator