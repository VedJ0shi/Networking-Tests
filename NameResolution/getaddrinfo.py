#establishing a socket object that connects/communicates with a server at a certain url
#use socket.getaddrinfo(url) to retrieve all coordinates sufficient to establish such a socket
import socket

'''socket coordinates are the values required for socket object construction and deployment'''

coord_list = socket.getaddrinfo('maps.google.com', 'www')

print(coord_list) #returns list of one or more tuples

ipv4_coordinates = coord_list[0] #chose first tuple bc it is for IPv4 TCP
print(ipv4_coordinates) #tuple will contain valid socket coordinates 
print()

print(ipv4_coordinates[0:3]) #coordintates for socket object creation, includes AF_INET
sock = socket.socket(*ipv4_coordinates[0:3])
print()

print(ipv4_coordinates[4]) #coordinate for connecting to url server
sock.connect(ipv4_coordinates[4])
print()

print(sock.getsockname())
print(sock.getpeername()) #socket connected as expected
sock.close()

'''getaddrinfo(url) returns tuples containing coordinates required for a socket
to connect with the url server; first tuple typically for IPv4 TCP sockets'''

'''first 3 items of a coordinates tuple as args for socket object constructor
and 5th item of tuple as remote address (IP addr, PORT) of url
'''