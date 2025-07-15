from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5

fx(5)
print(' done for 16')
fx(3)
print(' done for 3')
fx(10)
print(' done for 10')
fx(5)
print(' done for 16')
fx(3)
print(' done for 3')
fx(13)
print("Done for 13 ")
fx(10)
print(' done for 10')