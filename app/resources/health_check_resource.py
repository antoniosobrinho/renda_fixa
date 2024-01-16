from flask_restful import Resource
from models.investment_simulation import InvestmentSimulation
import psutil

class HealthCheckResource(Resource):

    def get(self):

        try:
            mongo_health = {'mongo': 'OK' if InvestmentSimulation.objects.first() else 'NOT OK'}

            memory_health = {'memory_percent': psutil.virtual_memory().percent}

            disk_health = {'disk_percent': psutil.disk_usage('/').percent}

            health_data = {
                'mongo': mongo_health,
                'memory': memory_health,
                'disk': disk_health
            }

            return health_data, 200
        except Exception as e:
            return {'error': str(e)}, 500