import socket

hostname = 'maps.google.com'
addr = socket.gethostbyname(hostname) #function that returns IP address of arg (expects url str)
print(f"IP address of {hostname} is:", addr)

'''if destination IP addr is not on loopback (127.*.*.*) or on local subnet,
then OS directs machine to forward packets to the local gateway, which connects to Internet'''