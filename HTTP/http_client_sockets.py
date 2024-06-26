#socket/IO-level HTTP client-- implements simple GET request/response pattern
import io, socket

class HTTPRequestConnection(socket.socket):

    def __init__(self, host, port=80):
        socket_args = (socket.AF_INET, socket.SOCK_STREAM)
        super().__init__(*socket_args)
        self.host = host
        self.port = port
    
    def send_GET(self):
        self.connect((self.host, self.port))
        print('connected to:', self.getpeername())
        request = f'GET / HTTP/1.1\r\nHost: {self.host}\r\n\r\n'   #Host header needed bc an IP address may virtually host multiple distinct domains
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
        output = HTTPResponseBuffer() 
        output.write(resp.decode())
        return output #returns a HTTPResponseBuffer instance containing raw response str




class HTTPResponseBuffer(io.StringIO):

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
        return '\r\n\r\n'.join(chunks[1:]) #in most cases, chunks list will only be split in two (headers + body)

