#program that checks if a web server at some url is indeed listening at port 80
import sys, socket

url_or_ip = sys.argv[1] #expects len(sys.argv) = 2

try:
    coord_list = socket.getaddrinfo(
        url_or_ip, 80, 0, socket.SOCK_STREAM, 0,
        socket.AI_ADDRCONFIG|socket.AI_V4MAPPED) #last arg are flags
    
except socket.gaierror: #when getaddrinfo() fails, it returns 'gaierror' exception
    sys.exit('name service failure')

coords = coord_list[0] #per standard recommendation, try first coords tuple
socket_args = coords[0:3]
remote_addr = coords[4]

sock = socket.socket(*socket_args)
try:
    sock.connect(remote_addr)
except socket.error: #when socket connection fails, it returns normal socket error
    sys.exit('network failure')
else:
    print(f"Success: Server of www.{url_or_ip} at address {remote_addr} listening on Port 80")

sock.close()
