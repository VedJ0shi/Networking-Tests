#socket in action
#both UDP client and server are on localhost 127.0.0.1
#127.0.0.0 – 127.255.255.255 are reserved for loopback, where communication managed within OS
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM refers to UDP datagrams

MAX = 65535 #max number of bytes to be read by socket in a single stream
PORT = 1060

if sys.argv[1] == "server":
    sock.bind(('127.0.0.1', PORT)) #server requests OS to grant it the given IP addr and Port
    print('Server listening at', sock.getsockname())
    while True:
        data, address = sock.recvfrom(MAX)
        print('Client at', address, 'says:', repr(data))
        sock.sendto(bytes(f'Your data was {len(data)} bytes', 'utf-8'), address)

elif sys.argv[1] == "client":
    sock.sendto(bytes('Arbitrary message', 'utf-8'), ('127.0.0.1', PORT))
    print ('Address after sending', sock.getsockname()) #OS automatically assigns ephemeral PORT to client when it calls sendto()
    data, address = sock.recvfrom(MAX) #client expects reply from server
    print ('Server at', address, 'says:', repr(data)) 

