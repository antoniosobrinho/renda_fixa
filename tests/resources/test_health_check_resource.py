from tests.setup_test import SetUpTest

class TestHeakthCheckResource(SetUpTest):

    def test_get_health_check(self):
        response = self.app.get('/health_check')
        self.assertEqual(response.status_code, 200)
        
