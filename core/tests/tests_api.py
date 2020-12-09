from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

FIBONACCI_URL = reverse('calculator:fibonacci')
FACTORIAL_URL = reverse('calculator:factorial')


class FibonacciApiTest(TestCase):

    # testing fibonacci functionality

    def setUp(self):
        self.api_client = APIClient()

    def test_no_input_provided(self):
        payload = {}
        res = self.api_client.post(FIBONACCI_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], "This field is required.")

    def test_non_integer_value(self):
        payload = {
            'n': 23.45
        }
        res = self.api_client.post(FIBONACCI_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], "A valid integer is required.")

    def test_pass_the_limit(self):
        payload = {
            'n': 50
        }
        res = self.api_client.post(FIBONACCI_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], 'you should provide number less than 35')

    def test_negative_input(self):
        payload = {
            'n': -23
        }
        res = self.api_client.post(FIBONACCI_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], 'you should enter non-negative numbers.')

    def test_success(self):
        payload = {
            'n': 14
        }
        res = self.api_client.post(FIBONACCI_URL, data=payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['success'], True)
        self.assertEqual(res.data['result'], 377)


class FactorialApiTest(TestCase):

    # testing factorial functionality

    def setUp(self):
        self.api_client = APIClient()

    def test_no_input_provided(self):
        payload = {}
        res = self.api_client.post(FACTORIAL_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], "This field is required.")

    def test_non_integer_value(self):
        payload = {
            'n': 23.45
        }
        res = self.api_client.post(FACTORIAL_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], "A valid integer is required.")

    def test_pass_the_limit(self):
        payload = {
            'n': 200
        }
        res = self.api_client.post(FACTORIAL_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], 'you should provide number less than 170')

    def test_negative_input(self):
        payload = {
            'n': -23
        }
        res = self.api_client.post(FACTORIAL_URL, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], 'you should enter non-negative numbers.')

    def test_success(self):
        payload = {
            'n': 7
        }
        res = self.api_client.post(FACTORIAL_URL, data=payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['success'], True)
        self.assertEqual(res.data['result'], 5040)