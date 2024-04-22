#single threaded event-driven server that monitors multiple connection sockets for communication
#pounces on the sockets that are actually ready to receive/send data
#different approach than threading, which can lead to race conditions and volatility
import launcelot_base as launcelot
import logging, select
#select module provides access to select() & poll() I/O multiplexing in the OS


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sock = launcelot.setup(5) #listening socket with backlog of 5
    sockets = [sock] #list of primary listening socket + accepted connection sockets
    count = 0
    while True:
        '''select() will poll and return only the event-updated sockets, including original listening socket'''
        read_sockets, _ , _ = select.select(sockets, [], []) #returns subset of sockets
        for read_sock in read_sockets:
            if read_sock == sock: #if listening socket has handshaked connection ready to be accepted from backlog
                conn, _ = sock.accept()
                f_d = conn.fileno() #returns file descriptor (uniquely identifiy int) of connection socket
                logging.info(f'connection with client {f_d} accepted')
                sockets.append(conn)
            else: #if connection socket has data in receive buffer
                try:
                    question = launcelot.recv_until(read_sock, '?')
                    answer = launcelot.qa_dict[question.decode()]
                    read_sock.sendall(answer.encode()) #assuming that send() will not block (good assumption for this case)
                except EOFError:
                    logging.info(f'connection with client {read_sock.fileno()} closed')
                    read_sock.close()
                    sockets.remove(read_sock)
                    continue














