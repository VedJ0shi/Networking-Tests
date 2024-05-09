#implements many-to-one request-response messaging
import zmq
import sys, time
#https://libzmq.readthedocs.io/en/zeromq3-x/zmq_socket.html

context = zmq.Context()

if sys.argv[1] == 'responder':
    '''REP type zsocket allows for bidirectional communication but
    constrained to the receive, send, receive, send... pattern'''
    '''Requests received are Fair-queued among all clients & 
    Responses are routed to the most-recently requesting client (Last-peer)'''
    
    zsock = context.socket(zmq.REP) #a REP server zsocket
    zsock.setsockopt(zmq.LINGER, 0) 
    zsock.bind('tcp://127.0.0.1:5555') 

    while True:
        msg = zsock.recv() #receive first before responding
        print('Received request:', msg)
        time.sleep(.5)
        zsock.send_string('Hello client')
        print('Sent a response')

if sys.argv[1] == 'requester': #can have multiple of these running
    '''REQ type zsocket allows for bidirectional communication but
    constrained to the send, receive, send, receive... pattern'''
    '''Requests sent are Round-robined among all servers'''

    zsock = context.socket(zmq.REQ) #a REQ server zsocket
    zsock.setsockopt(zmq.LINGER, 0)
    zsock.connect('tcp://127.0.0.1:5555') #can connect to multiple endpoints

    while True:
        print('Sending request')
        zsock.send_string('Hello server') #send first before receiving
        msg = zsock.recv()
        print('Received response:', msg)