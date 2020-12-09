from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

FIBONACCI_URL = reverse('calculator:fibonacci')
FACTORIAL_URL = reverse('calculator:factorial')
ACKERMANN_url = reverse('calculator:ackermann')


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
        self.assertEqual(res.data['n'][0], 'you should provide number less than 20')

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


class AckermannApiTest(TestCase):

    # testing ackermann functionality

    def setUp(self):
        self.api_client = APIClient()

    def test_no_input_provided(self):
        payload = {}
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], "This field is required.")
        self.assertEqual(res.data['m'][0], "This field is required.")

    def test_m_not_provided(self):
        payload = {
            'n': 23
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['m'][0], "This field is required.")

    def test_n_not_provided(self):
        payload = {
            'm': 3
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], "This field is required.")

    def test_non_integer_values(self):
        payload = {
            'n': 23.45,
            'm' : 1.5
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], "A valid integer is required.")
        self.assertEqual(res.data['m'][0], "A valid integer is required.")

    def test_pass_the_limit1(self):
        payload = {
            'n': 10000000,
            'm': 2
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], 'you should provide value for n less than 100000')

    def test_pass_the_limit2(self):
        payload = {
            'n': 10000,
            'm': 7
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['m'][0], 'you should provide value for m less than 4')

    def test_pass_the_limit3(self):
        payload = {
            'n': 250,
            'm': 3
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            res.data['non_field_errors'][0],
            'With m=3 you could choose value for n between 0 and 60'
        )

    def test_pass_the_limit4(self):
        payload = {
            'n': 250,
            'm': 4
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            res.data['non_field_errors'][0],
            'With m=4 you could choose 0,1 for n'
        )

    def test_negative_input(self):
        payload = {
            'n': -23,
            'm': -2
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data['n'][0], 'you should enter non-negative numbers.')
        self.assertEqual(res.data['n'][0], 'you should enter non-negative numbers.')

    def test_success1(self):
        payload = {
            'm': 2,
            'n': 200
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['success'], True)
        self.assertEqual(res.data['result'], 403)

    def test_success2(self):
        payload = {
            'm': 1,
            'n': 200
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['success'], True)
        self.assertEqual(res.data['result'], 202)

    def test_success3(self):
        payload = {
            'm': 0,
            'n': 200
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['success'], True)
        self.assertEqual(res.data['result'], 201)

    def test_success4(self):
        payload = {
            'm': 4,
            'n': 1
        }
        res = self.api_client.post(ACKERMANN_url, data=payload)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['success'], True)
        self.assertEqual(res.data['result'], 65533)