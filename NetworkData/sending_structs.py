import sys, socket, struct, time
#sending ints and floats as C Structs (work with fixed-size bytes in memory) over the network

'''client packs & sends stream of powers of 1/2 to server over TCP connection'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
HOST = '127.0.0.1'
PORT = 1060

def recv_all(sock, size):
    '''reliably returns exactly size length of bytes from socket's receive buffer'''
    received = b''
    while len(received) <= size:
        incoming = sock.recv(size -len(received))
        if incoming == b'': #EoF triggered prematurely
            break
        received = received + incoming #concatenates bytes
    return received



if sys.argv[1] == 'client':
    sock.connect((HOST, PORT))
    seq = [(1/2)**n for n in range(1,51)] #50 floats to be packed
    length = len(seq)*struct.calcsize('f') #length is number of bytes to be sent
    sock.shutdown(socket.SHUT_RD)
    sock.sendall(struct.pack('i', length)) #sends bytes
    time.sleep(1)
    byte_stream = struct.pack(f'{len(seq)}f', *seq) #floats in seq are given as parameters to .pack()
    sock.sendall(byte_stream)
    sock.close()

elif sys.argv[1] == 'server':
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind((HOST, PORT))
    sock.listen(1)
    sock_conn, _ = sock.accept()
    sock_conn.shutdown(socket.SHUT_WR)
    header = sock_conn.recv(1024)
    length = struct.unpack('i', header)[0] #.unpack() returns tuple, even if its one item
    print(f'Client will be sending {length} bytes of data...')
    byte_stream = recv_all(sock_conn, length)
    data = struct.unpack(f'{int(length/struct.calcsize("f"))}f', byte_stream)
    print(f"data is of type {type(data[0])}")
    for d in data:
        print(d)

    sock_conn.close()
    sock.close()

    










