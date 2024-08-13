import time 
import timeit

def do_something(): 
    for i in range(10): 
        x: int = i ** i 
        
def get_time(func: str, repeat: int, number: int) -> float: 
    speed: float = min(timeit.repeat(func, repeat=repeat, number=number, globals=globals()))
    print(f'{func}--> takes {speed:,} seconds time and ran {repeat*number:,} times')
    
    return speed

if __name__ == '__main__': 
    get_time("do_something()", number=1000, repeat=10000)
    
                       