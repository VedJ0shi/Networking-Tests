import concurrent.futures as cfutures
import time

def hanging_func(t):
    print('Sleeping...')
    time.sleep(t)
    print('...Woke up')

print('start of program')
start = time.perf_counter()

with cfutures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(hanging_func, [5]*10) #1st arg is the target given to run on each thread
#typicaly want max_workers to equal length of list/iterable passed to map()
#ThreadPoolExecutor handles exceptions in each thread internally
#joins are executed by context manager

end = time.perf_counter()
print(f'end of program, finished in {end-start}s')