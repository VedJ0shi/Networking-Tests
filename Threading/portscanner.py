#scans for open ports on a machine
import socket, threading
from queue import Queue

HOST = '192.168.1.1'

def scan(PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT)) #network operation--> blocking call that returns once TCP handshake completes   
    except:
        sock.close()
        return False
    else:
        sock.close()
        return True

q_flag = input('Use multithreading and queues, y/n? ')

if q_flag == 'n': #slow approach
    for port_num in range(1, 1024): #reserved range (for known services i.e. http, https, ssh, smtp)
        result = scan(port_num) #scans each port sequentially, which includes a wait-time for connect() call
        if not result:
            print(f'Port {port_num} is closed')
        else:
            print(f'Port {port_num} is open')


elif q_flag == 'y':
    myqueue = Queue() #FIFO queue object
    open_ports = []

    def fill_queue(port_list):
        for port_num in port_list:
            myqueue.put(port_num)
    
    def worker():
        while not myqueue.empty():
            port_num = myqueue.get() #pops off and returns next available item in queue
            if not scan(port_num): #OS will switch threads inside the scan() call
                print(f'Port {port_num} is closed')
            else:
                print(f'Port {port_num} is open')
                open_ports.append(port_num)


    fill_queue(range(1, 1024))

    for _ in range(10): #new worker function will run on each thread, but reads from same Queue object
        T = threading.Thread(target=worker) 
        T.start() 

    #threading will allow multiple connect() calls waiting in background at once
