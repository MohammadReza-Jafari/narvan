import os
from decimal import Decimal
import time
from datetime import datetime

from django.conf import settings
from core.models import Report


def timeit(func, currently_evaluating=None):

    """ this decorator calculate time that took by each function"""

    if currently_evaluating is None:
        currently_evaluating = set()

    def wrapper(*args, **kwargs):

        if func in currently_evaluating:
            return func(*args, **kwargs)
        else:
            start_time = time.time()
            currently_evaluating.add(func)
            try:
                value = func(*args, **kwargs)
            finally:
                currently_evaluating.remove(func)
            end_time = time.time()

            # save time of run in BASE_DIR/Reports/log.txt
            path = os.path.join(settings.BASE_DIR, 'Reports\\log.txt')
            if not os.path.exists(path):
                try:
                    os.makedirs(os.path.join(settings.BASE_DIR, 'Reports'))
                except OSError:
                    pass
            file = open(path, mode='a')

            res = ''
            for item in kwargs:
                res += f'{item}={kwargs[item]} ,'

            time_spent = Decimal(round((end_time-start_time), 4)) * 1000
            file.write(f"Date: {datetime.now()} => {func.__name__} took"
                       f" {time_spent} ms with input(s): {res} and result ={value} \n")
            file.close()

            # save the result in Database
            report = Report(
                func_name=func.__name__,
                time_spent=time_spent,
                inputs=res,
                result=value
            )
            report.save()
            return value
    return wrapper


@timeit
def fibonacci(n=0):
    """calculate fibonacci number"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


@timeit
def factorial(n=0):
    """calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


@timeit
def ackermann(m=0, n=0):
    """calculate ackermann function result"""
    if m == 0:
        return n+1
    if m == 1:
        return n+2
    if m == 2:
        return 2*n + 3
    if m == 3:
        return pow(2, n+3) - 3
    if m == 4 and n == 0:
        return 13
    if m == 4 and n == 1:
        return 65533
