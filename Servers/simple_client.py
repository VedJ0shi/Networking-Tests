#simple client that asks Launcelot server each of the 3 questions, then disconnects
import launcelot_base as launcelot
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 2:
    sys.exit('need to input server hostname as command line arg')
hostname = sys.argv[1]


sock.connect((hostname, launcelot.PORT))
sock.sendall(launcelot.qa[0][0].encode())
answer1 = launcelot.recv_until(sock, '.') #as per protocol, answers end with '.'
sock.sendall(launcelot.qa[1][0].encode())
answer2 = launcelot.recv_until(sock, '.')
sock.sendall(launcelot.qa[2][0].encode())
answer3 = launcelot.recv_until(sock, '.')
sock.close() #triggers EOF at server's receive buffer
print(answer1.decode())
print(answer2.decode())
print(answer3.decode())

