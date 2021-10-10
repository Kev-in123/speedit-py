__author__ = "Kev-in123"
__title__ = "speedit-py"
__license__ = "MIT"
__copyright__ = "Copyright 2021 Kev-in123"
__version__ = "1.1.1"

from time import perf_counter
from asyncio import run

def speed(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
          run(func(*args, **kwargs))
        except ValueError:
          func(*args, **kwargs)
        end = perf_counter()
        print(f"Function \"{func.__name__}\" took {end-start} seconds to complete")
    return wrapper
