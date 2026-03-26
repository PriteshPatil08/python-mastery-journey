# This program implements a retry mechanism using decorators to handle transient failures in function execution.
# It demonstrates advanced Python concepts like decorators, exception handling and function wrapping.
# It retries failed operations with an exponential backoff strategy to prevent system overload.
# You will learn how to build resilient, production-ready function wrappers for unreliable systems.

from functools import wraps
import time
import random

def retry(max_attempts : int, delay : float):
    def decorator(func):

        @wraps(func)        
        def wrapper(*args, **kwargs):
            attempt = 1
            current_delay = delay

            while attempt <= max_attempts:                
                try:
                    func(*args, **kwargs)
                    break
                except Exception as e:
                    if attempt < max_attempts:
                        print(f"❌ API call failed... Trying again")
                    else:
                        print("Please try again after sometime.")
                        raise e
                    
                    attempt += 1
                    time.sleep(current_delay)
                    current_delay *= 2                    
        return wrapper
    
    return decorator
        
@retry(max_attempts = 3, delay = 2.0)
def unstable_api() -> None:
    print("⏳ Calling API...")
    time.sleep(2)
    success = random.choice([True, False])

    if success:
        print("✅ API call complete")
    else:
        raise Exception("❌ API call failed!!!")

# Calling the unstable API.
unstable_api()