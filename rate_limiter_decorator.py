# This program implements a rate limiter using decorators to control how often a function can be called.
# It demonstrates advanced Python concepts like closures, decorators and function wrapping.
# It tracks call timestamps and enforces a limit within a sliding time window.
# You will learn how to build reusable, production-style function modifiers.

import time
from functools import wraps

def rate_limit(max_calls, period):
    def decorator(func):
        calls = []

        @wraps(func)
        def wrapper(*args, **kwargs):

            now = time.time()
            nonlocal calls

            calls = [i for i in calls if now - i < period]
            
            if len(calls) >= max_calls:
                raise Exception("Call Rate Limit reached. Calm down, tiger!!!")
            
            calls.append(now)
            func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls = 3, period = 5)
def greet(name):
    print(f"Hello, {name}!")

            
for i in range(5):
    try:
        greet("Pritesh")
    except Exception as e:
        print(e)