import threading
import time

#https://realpython.com/intro-to-python-threading/#starting-a-thread

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


flag = input('Run on two threads, y or n? ')

if flag == 'n': #running on 1 thread
    print('start of program')
    start = time.perf_counter()
    hanging_func(5)
    print(my_computation(1000))
    end = time.perf_counter()
    print(f'end of program, finished in {end-start}s')

elif flag == 'y': #runs hanging_func on separate thread; computation runs on main thread
    d_flag = input('Run second thread as a daemon, y or n? ')
    if d_flag ==  'n':
        print('start of program')
        start = time.perf_counter()
        X = threading.Thread(target=hanging_func, args=(5,))
        X.start() #switches to X thread which runs hanging function
        print(my_computation(100000)) #returns to main thread to do computation
        end = time.perf_counter()
        print(f'end of program, finished in {end-start}s')
        '''by default, X is a non-daemonic thread--
        a process will wait for all its non-daemonic threads to complete before it exits'''
    
    elif d_flag == 'y':
        print('start of program')
        start = time.perf_counter()
        X = threading.Thread(target=hanging_func, args=(5,), daemon=True)
        X.start() 
        print(my_computation(100000))
        end = time.perf_counter()
        print(f'end of program, finished in {end-start}s')
        '''X is a daemon-- process will exit and kill daemonic threads once main thread completes '''