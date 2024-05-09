#implements one-to-many fan out messaging from single publisher to multiple subscribers
import zmq
import sys, time, random

context = zmq.Context()

if sys.argv[1] == 'publisher':
    '''PUB type zsocket is unidirectional (send-only)'''
    '''Published messages are routed via fan out'''

        
    zsock = context.socket(zmq.PUB) #a PUB server zsocket; will publish to multiple topics
    zsock.setsockopt(zmq.LINGER, 0) 
    zsock.bind('tcp://127.0.0.1:5555') 

    while True:
        #topic is randomly generated integer, representing location id
        #pretending that publisher routes incoming sensor data from one of 5 locations
        sensor_data, topic = (random.randint(-100, 100), random.randint(0, 4))
        print(f'Sending data from location id-{topic}: {sensor_data}')
        zsock.send_string(f'{topic} {sensor_data}') #published, message starts with topic
        time.sleep(.5)
        


if sys.argv[1] == 'subscriber' and len(sys.argv) == 3: #multiple instances of these running (and multiple may be subscribed to same topic)
    '''SUB type zsocket is unidirectional (receive-only) and
    can be subscribed to particular incoming messages via filtering by topic'''

    topic = sys.argv[2] #topic specified by a integer 0-4
    zsock = context.socket(zmq.SUB) #a SUB server zsocket; will subscribe to the topic
    zsock.setsockopt_string(zmq.SUBSCRIBE, topic) #subscribed
    zsock.connect('tcp://127.0.0.1:5555')

    print(f'Collecting data for location id-{topic}')
    while True:
        #pretending that each subscriber handles data processing for a particular location
        msg = zsock.recv()
        print(f'Received and processing data')







