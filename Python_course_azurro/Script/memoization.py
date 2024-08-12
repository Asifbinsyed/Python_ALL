# It will help you to speed up our program. but it will take extra memory 

from functools import wraps 
from time import perf_counter
import sys
import functools
def memoize(func): 
    cache: dict = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs): 
        key: str = str(args) + str(kwargs)
        if key not in cache: 
            cache[key] = func(*args, **kwargs)
        
        return cache[key]
    return wrapper

@memoize
def fibonacchi(n) -> int: 
    if n<2: 
        return n 
    return fibonacchi(n-1)+ fibonacchi(n-2)

# Functools.cache also use the same thing 
@functools.cache
def fibonacchi_2(n) -> int: 
    if n<2: 
        return n 
    return fibonacchi_2(n-1)+ fibonacchi_2(n-2)


if __name__== "__main__": 
    start: float = perf_counter()
    f: int = fibonacchi(35)
    
    end: float = perf_counter()
    print(f)
    print(f"the time needed for running the program {end - start} ")
    