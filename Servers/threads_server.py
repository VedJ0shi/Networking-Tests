#multi threaded server in which each thread runs its own accept() call
#thus, each thread controls its own connection socket
import launcelot_base as launcelot
import logging, threading

def accept_client(sock):
    conn, _ = sock.accept() #multiple threads calling .accept() on the same listening socket
    logging.info(f'connection with client {conn.fileno()} accepted')

    def handle_client(): 
        try:
            while True:
                question = launcelot.recv_until(conn, '?') #blocking call-- OS may switch threads here
                answer = launcelot.qa_dict[question.decode()] 
                conn.sendall(answer.encode())  #blocking call-- OS may switch threads here
        except EOFError: 
            logging.info(f'connection with client {conn.fileno()} closed')
            conn.close()

    handle_client()
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sock = launcelot.setup(5)
    T1 = threading.Thread(target=accept_client, args=(sock,))
    T2 = threading.Thread(target=accept_client, args=(sock,))
    T1.start()
    T2.start() #alternatively, use ThreadPool

    '''threading is no longer safe (outcomes become volatile) if the 
    various threads of control are accessing and updating shared data structures
    or need to exchange messages with each other'''
