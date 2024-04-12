#printing out the list of possible "Address Families" available to a socket
import socket

print("address families:",dir(socket)[0:10])

'''IPv4 networking sockets (TCP/ UDP) use AF_INET (provided when socket object constructed) AND expect 
traditional 4 byte IPv4 addresses when socket tries to connect or bind (when socket object deployed for use) '''