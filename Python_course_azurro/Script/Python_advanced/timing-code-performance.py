import time 

start:time = time.perf_counter()
for i in range(10^5): 
    pass
time.sleep(1)

end: time = time.perf_counter()

print(f" the time needed for executing this code is {end - start}")

if __name__ == '__main__': 
    print("hello")

