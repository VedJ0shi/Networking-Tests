#implements pipeline where producer pushes messages to downstream workers, which then push result messages to a downstream sink 
import zmq
import sys, time, random

context = zmq.Context()

def run_producer():
    '''PUSH type zsocket is unidirectional (send-only)'''
    '''Outgoing messages are Round-robined across all downstream nodes'''

    zsock = context.socket(zmq.PUSH)
    zsock.bind('tcp://127.0.0.1:5555')

    for _ in range(20): #generates 20 numbers to be sent downstream
        val = random.randint(0, 100)
        print('Generated:', val)
        task_message = {'val': val}
        zsock.send_json(task_message)


def run_worker(unique_id):
    '''PULL type zsocket is unidirectional (receive-only)'''
    '''Incoming messages across all upstream nodes are Fair-queued'''

    print(f'I am worker #{unique_id}')
    receiver = context.socket(zmq.PULL)
    receiver.connect('tcp://127.0.0.1:5555') #downstream from producer at port 5555
    sender = context.socket(zmq.PUSH)
    sender.connect('tcp://127.0.0.1:5556') #upstream from sink at port 5556
    
    while True:
        task_message = receiver.recv_json()
        val = task_message['val']
        time.sleep(2) #emulates an expensive computation
        to_sink = {'consumer id': unique_id, 'result': val**val}
        print('Result of heavy task:', val**val)
        sender.send_json(to_sink)


def run_sink():
    zsock = context.socket(zmq.PULL)
    zsock.bind('tcp://127.0.0.1:5556')

    for _ in range(20): #know apriori the number of tasks sent by producer
        to_sink = zsock.recv_json()
        print(f'Received result {to_sink['result']} from worker {to_sink['consumer id']}')



if sys.argv[1] == 'producer':
    run_producer()

if sys.arv[1] == 'worker' and len(sys.argv) == 3: #run two or more instances of intermediate workers
    run_worker(sys.argv[2]) 

if sys.argv[1] == 'sink':
    run_sink()