from flask_restful import Resource
from flasgger import swag_from
from services.health_check_service import HealthCheckService
class HealthCheckResource(Resource):

    @swag_from('../swagger/health_check/get.yml')
    def get(self):
 
        service = HealthCheckService()

        health_data = service.get_health_check()
        
        return health_data, 200
     