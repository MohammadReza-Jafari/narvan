import os
import time
from datetime import datetime

from django.conf import settings


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
            file.write(f"Date: {datetime.now()} => {func.__name__} took"
                       f" {float((end_time-start_time))* 1000} ms with input(s): {res} \n")
            file.close()
            return value
    return wrapper

