import socket, sys, threading, datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 55555

def broadcast(message, room): 
    #expects message to be bytes object, room to be a dict mapping client nicknames to connection socket objects
    for client_name in room:
        room[client_name].sendall(message)

def handle(client_name, room):
    while True:
        try:
            message = room[client_name].recv(1024)
            broadcast(message, room)
        except: #recv() raises exception if peer socket no longer connected
            client_sock = room.pop(client_name)       
            print(f'Closing out {client_name} at address {room[client_name].getpeername()}')
            client_sock.close()
            broadcast(f'{client_name} left chat'.encode(), room)
            break

def receive(sock, room): #expects sock to be a listening socket
    '''main function at server end'''
    while True:
        sock_conn, peer_addr = sock.accept()
        timestamp = datetime.datetime.now()
        sock_conn.sendall(b'connection made')
        nickname = sock_conn.recv(1024).decode() #as per chatroom protocol
        room[nickname] = sock_conn #adds new connection socket object to the dict
        print(f'{nickname} is at address {peer_addr}, timestamp:{timestamp.time()}')
        broadcast(f'{nickname} joined the chatroom!'.encode(), room)
        T = threading.Thread(target=handle, args=(nickname, room))
        T.start()



if sys.argv[1] == 'server':
    '''server's job is to receive individual messages and then broadcast them on all connections'''
    sock.bind((HOST, PORT))
    sock.listen()
    myroom = {} #maintains info on live connections at server end
    receive(sock, myroom)
    #new client connections are received (receive function) by main thread
    #further communications with clients (handle function) are run on secondary threads

#######################################################################################


def write(sock, client_name): #expects sock to be connected to a server
    while True:
        text = f'{client_name}: {input("")}'
        sock.sendall(f'{text}'.encode())

def read(sock): #expects sock to be connected to a server
    while True:
        try:
            message = sock.recv(1024)
            print(message.decode())
        except:
            print('Server dropped connection')
            sock.close()
            break


if sys.argv[1] == 'client':
    sock.connect((HOST, PORT))
    message = sock.recv(1024)
    print(message.decode())
    if message == b'connection made': #first step in chatroom protocol
        nickname = input('Choose a nickname: ')
        sock.sendall(nickname.encode())
    else:
        sock.close()
        sys.exit('Oops this is us, please run client again')
    
    T1 = threading.Thread(target=read, args=(sock, ))
    T2 = threading.Thread(target=write, args=(sock, nickname))
    T1.start()
    T2.start()