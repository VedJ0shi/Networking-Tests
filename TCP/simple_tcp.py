#client and server built on top of TCP
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 1060
HOST = '127.0.0.1' #localhost

def recv_all(sock, length):
    data = b''
    while len(data) < length: #recv() call has to be within loop to avoid partial reception due to occupied buffer
        newdata = sock.recv(length-len(data))
        if newdata == None:
            raise EOFError(f'Socket close {len(data)} bytes into a {length} message')
        data = data + newdata
    return data

if sys.argv[1] == "server":
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT)) #server listening on localhost (loopback interface)
    sock.listen(1)
    while True:
        print("Listening at:", sock.getsockname())
        sc, sockname = sock.accept() #accept() is a network operation; sc is the returned socket representing newly accepted connection
        print("Accepted connection from:", sockname)
        print(f"Public socket connects {sc.getsockname()} and {sc.getpeername()}")
        message = recv_all(sc, 16)
        print("Incoming 16 byte message says:", repr(message))
        sc.sendall(b"Farewell, client")
        sc.close()
        print("Reply sent, socket closed")

elif sys.argv[1] == "client":
    sock.connect((HOST, PORT)) #this IS a network operation; initiates 3-way handshake with server at (HOST, PORT)
    print("Client has been assigned socket name:", sock.getsockname())
    sock.sendall(b"Hi there, server") 
    reply = recv_all(sock, 16) #no try-except provision needed since TCP handles retransmission
    print("Server said:", repr(reply))
    sock.close()

