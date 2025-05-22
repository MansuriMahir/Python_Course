# why do we need decorators?

import time
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@performance 
def long_time():
    for i in range(10000000):
        i*5 

long_time() 

# @auth - decorator function
