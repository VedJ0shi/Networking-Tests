#client streams data to server, the latter only receives
#communication buffers in other direction are preliminarily shutdown (.shutdown())
#end-of-file at server's receiving buffer is triggered by closing client socket (.close())
import sys, socket

'''one way to frame a streaming session is triggering EoF event at the server end by 
closing socket at client end'''

HOST = '127.0.0.1'
PORT = 1060
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

if sys.argv[1] =='server':
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    sock_conn, raddr = sock.accept() #sock_conn is the returned public connected socket
    print("Server's local socket address:", sock_conn.getsockname())
    print("Accpeted connection from client socket at:",sock_conn.getpeername())
    sock_conn.shutdown(socket.SHUT_WR) #disables sending buffer; streaming session is one-way
    streamed = b''
    while True:
        message = sock_conn.recv(8192) #arbitrary value of 8k bytes
        if message == b'': #the EoF event generated when client closes socket, ends stream
            break
        streamed = streamed + message
    print("Streaming session ended by client. Here is the received message:", streamed.decode())
    sock_conn.close()
    sock.close() #alternatively done by using context managers

elif sys.argv[1] == 'client':
    sock.connect((HOST, PORT))
    print("Client's local socket address:", sock.getsockname())
    sock.shutdown(socket.SHUT_RD) #disables receiving buffer
    sock.sendall(b'Beautiful is better than ugly \n') #sending bytes objects (autoencoded via ASCII/UTF-8)
    sock.sendall(b'Explicit is better than implicit \n')
    sock.sendall(b'Simple is better than complex')
    sock.close() #initiates FIN and closing proceduring; triggers EoF at server



