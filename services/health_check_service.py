from services.i_health_check_service import HealthCheckInterface
from mongoengine.connection import get_connection
import psutil

class HealthCheckService(HealthCheckInterface):

    def get_health_check(self) -> dict:
        
        health_data = {
            'database_status': self.__get_data_base_health(),
            'memory_percent': self.__get_memory_percent(),
            'disk_percent': self.__get_dict_usage_percent()
        }

        return health_data
    
    def __get_data_base_health(self) -> str:

        try:
            connection = get_connection()
            connection.server_info() 
            db_status = 'connected'
        except Exception as e:
             db_status = 'down'

        return db_status
    
    def __get_memory_percent(self) -> float: 
        virtual_memory = psutil.virtual_memory()
        return virtual_memory.percent

    def __get_dict_usage_percent(self) -> float:
        disk_usage =  psutil.disk_usage('/')    
        return disk_usage.percent