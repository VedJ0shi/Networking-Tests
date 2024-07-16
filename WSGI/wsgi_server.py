import socket, threading
from io import StringIO
from wsgi_app import application


class ResponseHandler:
    def __init__(self):
        self.status_line = None
        self.headers = None 
    
    def __call__(self, body): #expects body to be list of strs
        return self.status_line + self.headers + ['\r\n'] + body

    def start_response(self, status, headers): #expects status to be str and headers to be list of tuples; values decided inside application script
        self.status_line= [f'HTTP/1.1 {status}\r\n']
        self.headers = [f'{header}: {value}\r\n' for header, value in headers]




def set_environ(conn, method, path, qstr, proto, headers, body):
    environ = {'REQUEST_METHOD': method,
               'PATH_INFO': path,
               'QUERY_STRING': qstr,
               'CONTENT-TYPE':headers.get('Content-Type'),
               'CONTENT-LENGTH':headers.get('Content-Length'),
               'SERVER_PROTOCOL': proto,
               'SERVER_NAME':conn.getsockname()[0],
               'SERVER_PORT':conn.getsockname()[1],
               'REMOTE_ADDR':conn.getpeername()[0],
               'wsgi.input':StringIO(body),
               'wsgi.version': (1,0)}
    return environ
    


def parse_http(http):
    status_line, *headers, _, body = http.split('\r\n')
    if len(body)==0:
        body = None
    method, path, proto = status_line.split()
    qstr = None
    if '?' in path:
        path, qstr = path.split('?')
    headers = {header: value for header, value in [item.split(':', maxsplit=1) for item in headers]}
    return method, path, qstr, proto, headers, body
    

def echo_requests(conn):
    print(f'receiving from client at {conn.getpeername()}')
    print(conn.recv(1024).decode())


def handle_requests(conn):
    while True:
        new = ResponseHandler()
        http = conn.recv(1024)
        if not http:
            break
        http = http.decode()
        request = parse_http(http)
        environ = set_environ(conn, *request)
        body = application(environ, new.start_response) #WSGI server-application boundary
        response = new(body)
        for line in response:
            conn.sendall(line.encode())



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind(('localhost', 8000))
    server_sock.listen()
    while True: # in 'serve-forever' mode
        conn, _ = server_sock.accept()
        #T = threading.Thread(target=echo_requests, args=(conn,))
        T = threading.Thread(target=handle_requests, args=(conn,))
        T.start()





