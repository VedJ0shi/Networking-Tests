#simple server that only serves one client at a time; others have to wait
import launcelot_base as launcelot
import logging


def handle_client(client_conn): #expects an accepted connection socket
    try:
        while True:
            question = launcelot.recv_until(client_conn, '?')
            answer = launcelot.qa_dict[question.decode()] #retrives corresponding answer from dict
            client_conn.sendall(answer.encode())
    except EOFError: #recv_until() internally raises EOFError
        client_conn.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    sock = launcelot.setup(5) #listening socket with backlog of 5
    count = 0
    while True: #only enters next iteration if client_conn closes (EOFError)
        conn, _ = sock.accept()
        count = count + 1
        handle_client(conn)
        logging.info(f'connection with client {count} closed')

'''if more than 5 clients attempt to connect with server, then the TCP handshake 
requests (SYN's) from these additional clients will be ignored until the listening socket
accepts the next handshaked connection from the backlog queue-- in this case one at a time'''




