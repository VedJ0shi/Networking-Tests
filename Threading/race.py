import concurrent.futures as cfutures
import threading, time

class MyFakeDatabase:
    '''keeps track of .value'''
    def __init__(self):
        self.value = 0

    def write(self, k):
        load_copy = self.value #self.value is not in local scope of .write() method
        load_copy = load_copy + k
        time.sleep(0.2) #OS will switch threads here
        self.value = load_copy

'''going to update the same database object from 2 distinct threads'''

db_wrapper = MyFakeDatabase()

flag = input('Test with ThreadPools, y or n? ')

if flag == 'y':
    with cfutures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(db_wrapper.write, 1) #increments db_wrapper.value by 1
        print('incremented value in database by 1')
        executor.submit(db_wrapper.write, -1) #decrements db_wrapper.value by 1
        print('decremented value in database by 1')

elif flag == 'n':
    T1 = threading.Thread(target=db_wrapper.write, args=(1,)) 
    T2 = threading.Thread(target=db_wrapper.write, args=(-1,) )
    T1.start()
    print('incremented value in database by 1')
    T2.start() #because of GIL (global mutex), T2 does not get interpreter until T1 pauses
    print('decremented value in database by 1')
    T1.join()
    T2.join()

print('db_wrapper.value:', db_wrapper.value )

'''both implementations cause race condition on db_wrapper.value, since 
threads are switched before the object attribute is updated in the first write call'''


'''Each thread has its own copy of all variables local to the target function BUT 
db_wrapper.write deals with an object attribute (non-local to the method)'''