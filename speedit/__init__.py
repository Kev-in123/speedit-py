__author__ = "Kev-in123"
__title__ = "speedit-py"
__license__ = "MIT"
__copyright__ = "Copyright 2021 Kev-in123"
__version__ = "1.0"

import time

def speed(func):
  def wrapper(*args, **kwargs):
      start = time.perf_counter()
      func(*args, **kwargs)
      end = time.perf_counter()
      print(f"Function \"{func.__name__}\" took {end-start} seconds to complete")
  return wrapper

