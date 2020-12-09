from django.test import TestCase
from core.models import Report

from datetime import datetime


class TestReportModelTest(TestCase):

    def test_create_report(self):
        report = Report(
            created_time=datetime.now(),
            func_name='fibo',
            inputs='n=5',
            result=23,
            time_spent=15.67
        )

        self.assertEqual(str(report), 'fibo')
