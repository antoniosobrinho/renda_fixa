from flask_restful import Resource
from models.investment_simulation import InvestmentSimulationModel
import psutil

class HealthCheckResource(Resource):

    def get(self):
        """
        Get an health check of the api
        ---
        responses:
            200:
                description: Investment insights
                schema:
                    properties:
                        database_status:
                            type: string
                            description: checks if database is connect
                        memory_percent:
                            type: number
                            description: percent of memory used
                        disk_percent:
                            type: number
                            description: percent of disk used
        """
        try:
            database_status = 'On' if InvestmentSimulationModel.objects.first() else 'NOT OK'

            memory_percent =  psutil.virtual_memory().percent

            disk_percent = psutil.disk_usage('/').percent

            health_data = {
                'database_status': database_status,
                'memory_percent': memory_percent,
                'disk_percent': disk_percent
            }

            return health_data, 200
        except Exception as e:
            return {'error': str(e)}, 500