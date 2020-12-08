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
                os.makedirs(os.path.join(settings.BASE_DIR, 'Reports'))
            file = open(path, mode='a')

            res = ''
            for item in kwargs:
                res += f'{item}={kwargs[item]} ,'

            time_spent = Decimal((end_time-start_time)) * 1000
            file.write(f"Date: {datetime.now()} => {func.__name__} took"
                       f" {time_spent} ms with input(s): {res} \n")
            file.close()

            report = Report(
                func_name=func.__name__,
                time_spent=time_spent,
                inputs=res
            )
            report.save()
            return value
    return wrapper

@timeit()
def fibonacci(n=0):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


