from functools import wraps 
from typing import Callable

def repeat(times: int): 
    """ Repeat function call x amount of times""" 
    
    def decorator(func: Callable): 
        @wraps(func)
        def wrapper(*args, **kwargs): 
            value = None 
            for _ in range(times): 
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

@repeat(2)
def func1(): 
    print("hello")
    
if __name__ == "__main__": 
    func1()
