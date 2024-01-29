from tests.setup_test import SetUpTest
from unittest.mock import patch

class TestHealthCheckResource(SetUpTest):

    @patch('services.health_check_service.HealthCheckService.get_health_check')
    def test_get(self, mock_get_health_check):

        expected_data = {
            'database_status': 'connected',
            'memory_percent': 50.0,
            'disk_percent': 75.0
        }

        mock_get_health_check.return_value = expected_data
       
        response = self.app.get('/health_check')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.get_json(), expected_data)