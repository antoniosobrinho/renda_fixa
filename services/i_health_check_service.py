from abc import ABC, abstractmethod

class HealthCheckInterface(ABC):
  
    @abstractmethod
    def get_health_check(self) -> dict:
        pass