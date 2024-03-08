#establishing HTTP web server on local machine (listening on all local IP interfaces at TCP Port 80)
import socket


'''from documentation: socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)'''
'''use host=None, to retrieve coordinates for creating server on local machine'''

coord_list = socket.getaddrinfo(None, 80,0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
print(coord_list)
coords = coord_list[1] #IPv4 coords
print(coords)

sock = socket.socket(*coords[0:3])
sock.bind(coords[4])
sock.listen(1)

print(sock.getsockname())

sock.close()