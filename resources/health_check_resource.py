from flask_restful import Resource
from flasgger import swag_from
from models.investment_simulation import InvestmentSimulationModel
import psutil

class HealthCheckResource(Resource):

    @swag_from('../swagger/health_check/get.yml')
    def get(self):
 
        database_status = 'On' if InvestmentSimulationModel.objects.first() else 'NOT OK'

        memory_percent =  psutil.virtual_memory().percent

        disk_percent = psutil.disk_usage('/').percent

        health_data = {
            'database_status': database_status,
            'memory_percent': memory_percent,
            'disk_percent': disk_percent
        }

        return health_data, 200
     