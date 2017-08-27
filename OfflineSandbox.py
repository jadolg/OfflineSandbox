# -*-coding:utf-8-*-
import logging
from functools import wraps
from urllib import request


SANDBOX = False

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def offline_sandbox_value(value, url=None):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if url:
                if connect_to(url):
                    return func(*args, **kwargs)
                else:
                    logging.debug('** Sandboxed '+func.__name__+'() with value: '+value)
                    return value

            elif SANDBOX:
                logging.debug('** Sandboxed ' + func.__name__ + '() with value: ' + value)
                return value
            else:
                return func(*args, **kwargs)

        return inner

    return decorator


def connect_to(url):
    try:
        request.urlopen(url)
        return True
    except Exception:
        return False
