#high-level HTTP client that implements GET request/response pattern
import urllib.request, urllib.parse

class HTTPRequestWrapper:

    def __init__(self, host):
        self.url = 'http://' + host
        self.resp = None

    def fetch(self, data={}):
        full_url = self.url
        if data:
            query_str = urllib.parse.urlencode(data)
            full_url = full_url + '?' + query_str
        self.resp = urllib.request.urlopen(full_url) #directly returns an HTTPResponse object (from http.client lib)
        text = self.resp.read().decode()
        return text


    
