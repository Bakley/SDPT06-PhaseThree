from colorama import Fore, Style, init
from functools import wraps

def colorize_output(color):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(color)
            result = func(*args, **kwargs)
            print(Style.RESET_ALL)
            return result
        return wrapper
    return decorator
