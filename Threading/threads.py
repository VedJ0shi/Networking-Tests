import threading


def hello(thread_name):
    print(f'{thread_name} thread: Hello world')

def repeat(func, arg):
    for _ in range(50):
        func(arg)


T1 = threading.Thread(target=hello, args=('T1',))
T2 = threading.Thread(target=hello, args=('T2',))
T3 = threading.Thread(target=repeat, args=(hello, 'T3'))

print('Main thread: Hello world')
T1.start()
T2.start()
T3.start()
print('Main thread: Hello again') #printed before T3 finishes all print statements; thread scheduling effect