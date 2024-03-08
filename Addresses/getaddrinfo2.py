import socket

coord_list = socket.getaddrinfo('upenn.edu', 'www')

coords = coord_list[0] #gets TCP socket coords
print(coords)

sock = socket.socket(*coords[0:3])
sock.connect(coords[4])

print(sock.getpeername())
sock.close()