import time
from functools import wraps

def executionTimer(func):
    @wraps(func)
    def timeWrapper(*args, **kwargs):
        beginTime = time.time()
        result = func(*args, **kwargs)
        completeTime = time.time()
        totalTime = completeTime - beginTime
        print("The", func.__name__, "method completed in:", totalTime)
        return result
    return timeWrapper

@executionTimer
def exampleMethod(n:int):
    while n != 100000:
        n += 1

print(exampleMethod(0))