#realistic client that retrieves and asks Launcelot server each of the 3 questions stored in fake database
#delays represent time to query database
import launcelot_base as launcelot
import socket, sys, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 2:
    sys.exit('need to input server hostname as command line arg')
hostname = sys.argv[1]

def retrieve_Question(k):
    fake_database = {1:launcelot.qa[0][0], 2:launcelot.qa[1][0], 3:launcelot.qa[2][0]}
    time.sleep(2) #delay
    return fake_database[k]


sock.connect((hostname, launcelot.PORT))
sock.sendall(retrieve_Question(1).encode())
answer1 = launcelot.recv_until(sock, '.') #as per protocol, answers end with '.'
print(answer1.decode())
sock.sendall(retrieve_Question(2).encode())
answer2 = launcelot.recv_until(sock, '.')
print(answer2.decode())
sock.sendall(retrieve_Question(3).encode())
answer3 = launcelot.recv_until(sock, '.')
print(answer3.decode())
sock.close() #triggers EOF at server's receive buffer


