# -*-coding:utf-8-*-

from functools import wraps

SANDBOX = True


def offline_sandbox_value(value):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if SANDBOX:
                return value
            else:
                return func(*args, **kwargs)

        return inner

    return decorator
