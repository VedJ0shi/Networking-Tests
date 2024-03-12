#confirming a forward name lookup with a reverse name lookup
'''a given hostname (url) need not necessarily work both forward and backward--
a service specific hostname may point to the IP addr of a 'real/canonical hostname' 
'''

import sys, socket

hostname = sys.argv[1] #expects len(sys.argv) = 2

try:
    coord_list = socket.getaddrinfo(
        hostname, 80, 0, socket.SOCK_STREAM, 0,
        socket.AI_ADDRCONFIG|socket.AI_V4MAPPED|socket.AI_CANONNAME) #last flag implies 'Canonical name' will be included in coordinates
    
except socket.gaierror: #when getaddrinfo() fails, it returns 'gaierror' exception
    sys.exit('name service failure')

coords = coord_list[0] #per standard recommendation, try first coords tuple
socket_args = coords[0:3]
remote_addr = coords[4]
canonical_name = coords[3]

if not canonical_name:
    sys.exit(f"Server of www.{hostname} at address {remote_addr} has no canonical name available for reverse lookup")
else:
    print(f"Server of www.{hostname} at address {remote_addr} has canonical name:", canonical_name)
    print(f"record: {remote_addr[0]} <-> {canonical_name} ")

if hostname.casefold() == canonical_name.casefold():
    print(f"Reverse lookup of IP addr {remote_addr[0]} should yield the forward hostname")
else:
    print(f"Reverse lookup of IP addr {remote_addr[0]} does not yield forward hostname!")

'''if hostname and canonical_name are sufficiently different, then one can assume
the hostname is purely symbolic and that the web servers are run on machines in 
a completely different 'domain'
 '''