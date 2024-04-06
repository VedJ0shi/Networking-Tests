import concurrent.futures as cfutures
import threading, time

#fixed race condition by implementing lock in the write method

class MyFakeDatabase:
    '''keeps track of .value'''
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def write(self, k):
        with self._lock:
            print('lock acquired')
            load_copy = self.value
            load_copy = load_copy + k
            time.sleep(0.2) #OS will not switch threads here, because lock is still acquired
            self.value = load_copy
            print('releasing lock')
        #lock released
        

db_wrapper = MyFakeDatabase()

with cfutures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(db_wrapper.write, 1) #increments db_wrapper.value by 1
    executor.submit(db_wrapper.write, -1) #decrements db_wrapper.value by 1

print('db_wrapper.value:', db_wrapper.value )

'''thread will hold lock while it sleeps (or some other background I/O) and
release lock only after it updates the value attribute'''