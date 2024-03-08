#establishing DNS server on loopback (listening on localhost at UDP Port 53)
import socket

'''from documentation: socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)'''

coord_list = socket.getaddrinfo('localhost', 53, 0, socket.SOCK_DGRAM, 0, 0)
print(coord_list)

coords = coord_list[1] #IPv4 coords
print(coords)

sock = socket.socket(*coords[0:3])
sock.bind(coords[4])

print(sock.getsockname())

sock.close()