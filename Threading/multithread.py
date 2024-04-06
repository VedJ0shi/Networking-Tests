import threading, time

def hanging_func(t):
    print('Sleeping...')
    time.sleep(t)
    print('...Woke up')

j_flag = input('Schedule new threads to end prior to main thread, y or n? ')

threads = []

print('start of program')
start = time.perf_counter()
for _ in range(10):
    T = threading.Thread(target=hanging_func, args=(5,))
    threads.append(T)
    T.start()

if j_flag == 'y':
    for _ in range(10):
        T.join()

end = time.perf_counter()
print(f'end of program, finished in {end-start}s')