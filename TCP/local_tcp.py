#client and server built on top of TCP
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM refers to TCP Streams
PORT = 1060
HOST = '127.0.0.1' #localhost


def recv_all(sock, length): #returns only once length bytes of data has accumulated in the buffer
    data = b''
    while len(data) < length: #recv() call has to be within loop to avoid partial reception due to occupied buffer
        newdata = sock.recv(length-len(data))
        if not newdata:
            raise EOFError(f'Socket close {len(data)} bytes into a {length} message')
        data = data + newdata
    return data

if sys.argv[1] == "server":
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT)) #server listening on localhost (loopback interface)
    sock.listen(1) #prepares socket for next accept() call; now sock is purely a 'listening socket'
    while True:
        print("Listening at:", sock.getsockname())
        sc, clientname = sock.accept() #accept() is a blocking call; sc is the returned socket representing newly accepted connection
        print("Accepted connection from:", clientname)
        print(f"Public socket connects {sc.getsockname()} and {sc.getpeername()}")
        message = recv_all(sc, 16) #expecting a fixed length 16 byte message
        #message = sc.recv(65535)
        print("Incoming 16 byte message says:", repr(message))
        sc.sendall(b"Farewell, client")
        sc.close() #concludes TCP session via FIN-ACK handshake
        print("Reply sent, socket closed")

elif sys.argv[1] == "client":
    sock.connect((HOST, PORT)) #this IS a network operation; initiates 3-way handshake with server at (HOST, PORT)
    print("Client has been assigned socket name:", sock.getsockname())
    sock.sendall(b"Hi there, server") 
    reply = recv_all(sock, 16) #no try-except provision needed since TCP handles retransmission
    print("Server said:", repr(reply))
    sock.close()

#https://stackoverflow.com/questions/17446491/tcp-stream-vs-udp-message
#https://stackoverflow.com/questions/65689312/why-does-accept-block-when-listen-is-the-very-first-involved-in-tcp
#https://www.reddit.com/r/learnpython/comments/o3ox88/what_really_is_recvbufsize/
#https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be



'''Note: for TCP streams, the bufsize arg in recv(bufsize) is the upper bound on the bytes 
 of the payload that can be read into memory from the byte stream in receive buffer; 
 may read in less bytes than bufsize if buffer has any data waiting in it-- 
 hence the use of recv_all() if a fixed message length known apriori'''