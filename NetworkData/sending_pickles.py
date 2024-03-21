import sys, socket, pickle, datetime
#sending objects as serialized Pickles over the network

'''client serializes & sends a complex dict object to server over TCP connection'''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
HOST = '127.0.0.1'
PORT = 1060


my_object = {
    'Name': 'John Doe',
    'IDN': 172937429,
    'DoB' : datetime.date(1997, 1, 20),
    'PoB' : 'United States',
    'Features' : ['black hair', 'green eyes', 'birthmark'],
    'Relations' : {'Mother': 'Jane', 'Father': 'John Sr.', 'Sister':'Jen'}
}

if sys.argv[1] == 'client':
    sock.connect((HOST, PORT))
    sock.shutdown(socket.SHUT_RD)
    byte_stream = pickle.dumps(my_object) #serializes the object
    sock.sendall(byte_stream)
    sock.close()

elif sys.argv[1] == 'server':
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind((HOST, PORT))
    sock.listen(1)
    sock_conn, _ = sock.accept()
    sock_conn.shutdown(socket.SHUT_WR)
    byte_stream = b''
    while True:
        incoming = sock_conn.recv(64)
        if incoming == b'':
            break
        byte_stream = byte_stream + incoming
    print(f'Client sent {len(byte_stream)} bytes of data...')
    unpickled = pickle.loads(byte_stream)
    for key in unpickled:
        print(key,',', unpickled[key], ',', type(unpickled[key]))




    sock_conn.close()
    sock.close()

    










