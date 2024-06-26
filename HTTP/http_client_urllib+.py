#high-level HTTP client that can facilitate simple GET and POST requests
#functionality for adding headers and request body
import urllib.request, urllib.parse

class HTTPRequestWrapper:

    def __init__(self, host):
        url = 'http://' + host
        self.req = urllib.request.Request(url) #Request object for building requests
        self.resp = None


    def fetch(self, method='GET', data={}, headers={}):  
        if method=='GET':
            if data:
                query_str = urllib.parse.urlencode(data)
                self.req.full_url = self.req.full_url + '?' + query_str
        elif method == 'POST':
            if not data:
                raise ValueError('Must include data in a POST request')
            self.req.data = urllib.parse.urlencode(data).encode()
            headers['Content-length'] =  len(self.req.data)
            headers['Content-type'] = 'application/x-www-form-urlencoded' #default encoding for HTML forms
        for h in headers:
                self.req.add_header(h, headers[h])  
        self.resp = urllib.request.urlopen(self.req)
        text = self.resp.read().decode()
        return text


            



