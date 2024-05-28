#socket/IO-level HTTP client-- implementing with simple GET request/response pattern
import  io, socket

#structure of requests/responses: https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages

class HTTPRequestConnection(socket.socket):
    '''handles a single GET request on Port 80'''

    def __init__(self, *args):
        super().__init__(*args)
        if len(args) < 2 or args[1] != socket.SOCK_STREAM:
            raise ValueError('supports stream sockets only; please set to SOCK_STREAM')
    
    def send_GET(self, host):
        self.connect((host, 80))
        print('connected to:', self.getpeername())
        request = f'GET / HTTP/1.1\r\nHost: {host}\r\n\r\n'   #Host header needed bc an IP address may virtually host multiple distinct domains
        self.sendall(request.encode())
        print('sent GET request to server')
    
    def recv_resp(self): #to be called only after .send_GET()
        resp = b''
        self.settimeout(2) 
        while True:
            try:
                stream = self.recv(1024)
                print('receiving response from server...')
                if not stream: #connection closed
                    break
            except: #blocking timeout expired
                break
            resp = resp + stream
        self.close()
        output = HTTPResponseBuffer() #inherits from StringIO
        output.write(resp.decode())
        return output #returns a HTTPResponseBuffer instance containing raw response str




class HTTPResponseBuffer(io.StringIO):
    '''interface to access a single GET response'''

    def headers(self):
        '''header chunk is terminated by a blank line'''
        s = self.getvalue() #inherited method that returns entire contents of buffer w/o affecting file position pointer
        chunks = s.split('\r\n\r\n')
        return chunks[0]
    
    def status(self):
        '''individual header lines concluded by the 2-byte cr-newline sequence'''
        h = self.headers()
        lines = h.split('\r\n')
        status_line = lines[0]
        items = status_line.split()
        return items[1], items[2]  #items[0] contains protocol version i.e. HTTP/1.1

    def content_length(self):
        h = self.headers()
        i = h.find('Content-Length')
        if i == -1:
            return
        j = h.find('\r', i)
        items = h[i:j].split()
        return int(items[1])

    def read(self):
        '''response body (request resource) comes after header chunk'''
        s = self.getvalue()
        chunks = s.split('\r\n\r\n')
        return '\r\n\r\n'.join(chunks[1:])

