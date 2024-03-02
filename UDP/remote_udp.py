#modeling remote server-client UDP communication with randomly dropped packets
import socket, sys, random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #opens UDP socket

MAX = 65535 
PORT = 1060

#server chooses to randomly answer only half of client requests
#server listening at port 1060 on all local IP interfaces 
if sys.argv[1] == "server":
    sock.bind(('', PORT)) #OS assigns IP addr 0.0.0.0 which means 'any local interface'
    print('Listening at:', sock.getsockname())
    while True:
        data, client_addr = sock.recvfrom(MAX)
        if random.randint(0,1) == 1:
            print(f"Client at {client_addr} says:", repr(data))
            sock.sendto(bytes(f'Your data was {len(data)} bytes', 'utf-8'), client_addr)
        else:
            print("Pretending to drop packets from client at", client_addr)



#client is localhost 127.0.0.1
elif sys.argv[1] == "client":
    server_addr = '127.0.0.55' #arbitrary IP addr on the loopback interface
    sock.connect((server_addr, PORT)) #not a network operation; only sets default send addr and response filter
    print('Sending requests from:',sock.getsockname()) #ephemeral PORT automatically assigned
    delay = 0.1
    while True:
        sock.send(bytes('This is another message', 'utf-8'))
        sock.settimeout(delay) #client informs OS it will not stay stuck in network operation (.recv() call) for more than delay seconds
        print(f'...waiting up to {delay} seconds for reply from server')
        try:
            data = sock.recv(MAX)
        except socket.timeout: #TimeoutError from network operation
            delay = delay + 0.1 #increases delay in order to adjust to potential congestion at server
            if delay >= 2.5:
                raise RuntimeError("Server might be down...")
        else: #executes if there's no exception
            break

    print('Server said:', repr(data))

