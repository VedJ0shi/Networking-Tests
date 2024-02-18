import socket

hostname = 'maps.google.com'
addr = socket.gethostbyname(hostname) 
print("IP address is:", addr)

'''if host IP addr is not localhost (127.*.*.*) or on local subnet,
then OS directs machine to forward packet to the local gateway, which connects to Internet'''