import threading
import time


def hanging_func(t):
    print('Sleeping...')
    time.sleep(t)
    print('...Woke up')

def my_computation(n):
    sum = 0
    start = time.perf_counter()
    while n >= 1:
        sum = sum + n
        n = n - 1
    end = time.perf_counter()
    return (sum, end-start)

print('start of program')
start = time.perf_counter()
X = threading.Thread(target=hanging_func, args=(5,))
X.start() #switches to X thread which runs hanging function
print(my_computation(100000)) #returns to main thread to do computation
X.join() #switches back to X thread and sets mutex until thread completes (until target finishes execution)
end = time.perf_counter()
print(f'end of program, finished in {end-start}s')