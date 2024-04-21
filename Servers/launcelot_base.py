#all functions and constants to be used for the 'Launcelot protocol'
import socket, sys

PORT = 1060
qa = (('What is your name?', 'My name is Sir Launcelot of Camelot.'), 
      ('What is your quest?', 'To seek the Holy Grail.'),
      ('What is your favorite color?', 'Blue.'))

qa_dict = dict(qa) 

def recv_until(sock, suffix):
    '''keeps receiving data from socket's buffer until a particular suffix char'''
    message = b''
    while not message.endswith(suffix.encode()):
        data = sock.recv(1024)
        if data == b'':
            raise EOFError(f'peer closed connection before we saw {suffix}')
        message = message + data
    return message


def setup(limit):
    '''establishes server socket'''
    if len(sys.argv) != 2:
        sys.exit('need to input server hostname as command line arg')
    interface = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    sock.bind((interface, PORT))
    sock.listen(limit)
    return sock #returns a listening socket obj with a limited backlog for handshaked connections

