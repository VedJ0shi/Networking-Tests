#exact same as smart_tcp BUT implements shutdown() to "half-close" the socket
#shutdown(socket.SHUT_WR) is a better alternative to settimeout() and try-except provisions
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
PORT = 1060
HOST = '127.0.0.1' 


if sys.argv[1] == "server": #expects len(sys.argv) = 3
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT)) 
    sock.listen(1) 
    while True:
        print("Listening at:", sock.getsockname())
        sc, clientname = sock.accept() #accept() is a blocking call
        print("Processing up to 1024 bytes from:", clientname)
        n=0
        while True:
            message = sc.recv(1024) #max 1024 byte reads as memory management safeguard
            if message == b'': #recv() returns empty iff client has begun closing connection, including "half-closing"
                print("byte stream finished")
                break
            if sys.argv[2] == "upper":
                foo = message.decode().upper()
            elif sys.argv[2] == "title":
                foo = message.decode().title()
            sc.sendall(foo.encode()) #sends processed message back to client
            n = n + len(message) #max len(message) is 1024
            print(f"{n} bytes processed from buffer so far")

        sc.close() #server initiates closing connection completely
        print("All transformed data sent, socket closed")
        



elif sys.argv[1] == "client": 
    sock.connect((HOST, PORT)) 
    print("Client has been assigned socket name:", sock.getsockname())
    repeat = "a"*16
    bytes_sent = 0;
    while bytes_sent < 48: #RHS is total length of byte stream that will be waiting in server's input buffer
        #RHS can cause communication deadlock if choice is too large
        sock.sendall(repeat.encode())
        bytes_sent = bytes_sent + len(repeat)
        print(f"Total {bytes_sent} bytes sent")
    sock.shutdown(socket.SHUT_WR) #"half-closes" socket; tells server one direction of communication is now closed
    print("Now receiving transformed data from server...")

    bytes_received = 0
    while True:
        data = sock.recv(8) #bufsize can be modified
        if data == b'': #in this case, recv() returns empty once server initiates close()
            print("byte stream finished")
            break
        bytes_received = bytes_received + len(data)
        print("Server sent back:", repr(data))
        print(f"Total {bytes_received} bytes received")   
    
    sock.close()


