#implements one-to-one messaging
import zmq #message-passing library
import sys, time
#docs: https://libzmq.readthedocs.io/en/zeromq3-x/

context = zmq.Context() #necessary to create associated zsockets

if sys.argv[1] == 'server':
    '''PAIR type zsocket can only be connected one peer at the port,
    allows for unconstrained bidirectional communication'''
    zsock = context.socket(zmq.PAIR) #a PAIR server zsocket
    zsock.setsockopt(zmq.LINGER, 0) #memory-related setting
    zsock.bind('tcp://127.0.0.1:5555') #binds to this endpoint (transport protocol is always given)

    while True:
        zsock.send_string('Hello client') #comm over 'strings' rather than raw streams
        msg = zsock.recv()
        print(msg)
        time.sleep(.5)



if sys.argv == 'client':
    zsock = context.socket(zmq.PAIR)
    zsock.setsockopt(zmq.LINGER, 0)
    zsock.connect('tcp://127.0.0.1:5555') 
   
    count = 0
    while count < 10:
        msg = zsock.recv()
        print(msg)
        zsock.send_string('Hello server')
        print('Counter:', count)
        count = count + 1
        time.sleep(.5)
        
    context.destroy()
    zsock.close()










