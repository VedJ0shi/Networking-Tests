import socket

coord_list = socket.getaddrinfo('upenn.edu', 'www')

coords = coord_list[0] #gets IPv4 TCP socket coords
print(coords)

sock = socket.socket(*coords[0:3]) #TCP socket object construction
sock.connect(coords[4]) #TCP connection with peer at www.upenn.edu

print(sock.getpeername())
sock.close()

