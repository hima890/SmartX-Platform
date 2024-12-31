from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.

class RateLimitTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.endpoint = '/contact-us/'  # Replace with your endpoint URL
        self.valid_payload = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'message': 'This is a test message.',
        }

    def test_rate_limiting(self):
        # Simulate hitting the endpoint multiple times
        for _ in range(5):
            response = self.client.post(self.endpoint, self.valid_payload)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn('success', response.data['status'])

        # The 6th request should be blocked
        response = self.client.post(self.endpoint, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        self.assertIn('Rate limit exceeded', response.data['message'])
