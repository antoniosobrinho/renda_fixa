from services.interfaces.i_health_check_service import HealthCheckInterface
from mongoengine.connection import get_connection
import psutil

class HealthCheckService(HealthCheckInterface):

    def get_health_check(self) -> dict:
        
        memory_percent =  self.__get_memory_percent()
        if memory_percent >= 80:
            memory_warnning = 'Limite de uso de memória saúdavel atingido'
        else:
            memory_warnning = 'Memória saúdavel'

        disk_percent = self.__get_dict_usage_percent()
        if disk_percent >= 80:
            disk_warnning = 'Limite de uso de disco saúdavel atingido'
        else:
            disk_warnning = 'Disco saúdavel'

        health_data = {
            'database_status': self.__get_data_base_health(),
            'memory_percent': memory_percent,
            'memory_warnning': memory_warnning,
            'disk_percent': disk_percent,
            'disk_warnning': disk_warnning
        }

        return health_data
    
    def __get_data_base_health(self) -> str:

        try:
            get_connection().server_info()
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