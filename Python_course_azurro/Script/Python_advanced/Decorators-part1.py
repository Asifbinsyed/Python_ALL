from functools import wraps 
from time import perf_counter, sleep
def get_time(func):
    """Time any function"""
    @wraps(func)
    def wrapper(*args, **qwargs):
        start_time:float= perf_counter
        func(*args, **qwargs)
        end_time:float = perf_counter
        
        total_time = round(end_time- start_time)
        print('Time: ', total_time, 'second')
    return wrapper    
        

def do_something(params):
    """ Do something important """
    sleep(1)
    print(params)
    
if __name__== "__main__":
    do_something("Hello") 