import unittest
from unittest.mock import Mock, patch
from services.health_check_service import HealthCheckService

class TestHealthCheckService(unittest.TestCase):

    def setUp(self):
        self.health_check_service = HealthCheckService()

    @patch('services.health_check_service.get_connection')
    def test_get_data_base_health_success(self, mock_get_connection):
        mock_get_connection.return_value.server_info.return_value = {}
        db_status = self.health_check_service._HealthCheckService__get_data_base_health()
        self.assertEqual(db_status, 'connected')

    @patch('services.health_check_service.get_connection')
    def test_get_data_base_health_exception(self, mock_get_connection):
        mock_get_connection.return_value.server_info.side_effect = Exception('Connection error')
        db_status = self.health_check_service._HealthCheckService__get_data_base_health()
        self.assertEqual(db_status, 'down')

    @patch('services.health_check_service.psutil')
    def test_get_memory_percent(self, mock_psutil):
        mock_virtual_memory = Mock()
        mock_virtual_memory.percent = 50.0
        mock_psutil.virtual_memory.return_value = mock_virtual_memory

        memory_percent = self.health_check_service._HealthCheckService__get_memory_percent()
        self.assertEqual(memory_percent, 50.0)

    @patch('services.health_check_service.psutil')
    def test_get_disk_usage_percent(self, mock_psutil):
        mock_disk_usage = Mock()
        mock_disk_usage.percent = 75.0
        mock_psutil.disk_usage.return_value = mock_disk_usage
        disk_percent = self.health_check_service._HealthCheckService__get_dict_usage_percent()
        self.assertEqual(disk_percent, 75.0)

    @patch('services.health_check_service.psutil')
    def test_get_health_check(self, mock_psutil):
        mock_virtual_memory = Mock()
        mock_virtual_memory.percent = 50.0
        mock_psutil.virtual_memory.return_value = mock_virtual_memory

        mock_disk_usage = Mock()
        mock_disk_usage.percent = 75.0
        mock_psutil.disk_usage.return_value = mock_disk_usage

        health_data = self.health_check_service.get_health_check()

        expected_health_data = {
            'database_status': 'connected',
            'memory_percent': 50.0,
            'disk_percent': 75.0
        }

        self.assertEqual(health_data, expected_health_data)

