#not an executable script; read only
'''below are all the major socket methods that deal with addresses'''

mysocket = "socket.socket(socket.AF_INET, ...) "
addr = ('IP addr', 'PORT')
data = b'data'
bufsize = 'some integer'

mysocket.accept()
'''
-mysocket must be a listening TCP stream socket
-blocking call that accepts handshaked connections from the backlog of listening socket
-returns 2-tuple whose 1st item is the connected socket object
 and 2nd item is the remote address of the newly connected peer 
'''

mysocket.bind(addr)
'''
-mysocket can be any socket
-assigns addr to be the local address of mysocket
-incoming connections and packets will have an address to connect() or sendto()
'''

mysocket.connect(addr)
'''
-mysocket can be any socket
-for UDP dgram sockets, sets default destination addr if socket calls send()
 instead of sendto() (also sets a recv() filter for incoming packets to emulate connection)
-for TCP stream sockets, this is an actual network operation that initiates the
 3-way Handshake with peer at remote addr (should be a listening socket at remote addr)
'''

mysocket.sendto(data, addr)
'''
-mysocket should be a UDP dgram socket
-allows mysocket to send packets to an unconnected peer at remote addr
'''


mysocket.recvfrom(bufsize)
'''
-mysocket should be a UDP dgram socket
-returns a 2-tuple whose 1st item is data from incoming datagram
 and 2nd item is remote address of peer
'''

mysocket.getsockname()
'''
-mysocket can be any socket
-returns local address of mysocket
'''

mysocket.getpeername()
'''
-mysocket should be a connected socket
-returns remote address of connected peer
'''

