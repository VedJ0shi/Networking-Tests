#printing out the list of possible "Address Families" available to a socket
import socket

print("address families:",dir(socket)[0:10])

'''IP networking sockets (TCP/ UDP) use AF_INET (provided when socket object created) and expect 
traditional 4 byte IPv4 addresses when socket tries to bind (when socket object deployed with .bind()) '''