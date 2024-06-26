#middle-level HTTP client
import http.client

conn = http.client.HTTPConnection("www.google.com", 80)
conn.request("GET", "/", headers={'Host':'www.google.com'})
resp = conn.getresponse() #returns an HTTPResponse instance
print(resp.status, resp.reason) #HTTPResponse instance methods
print(resp.getheaders(), resp.getheader('Content-length'), resp.getheader('Content-type') )

data = resp.read()  # This will return entire content as a bytes object
print(data[:500], type(data)) #return first 500 bytes 

#can make subsequent requests on same HTTPConnection using same underlying socket (HTTP 1.1 default is Keep-alive)
conn.request("GET", "/about", headers={'Host':'www.google.com'})
resp = conn.getresponse() 
print('after consecutive request:', resp.status, resp.reason)

conn.close()

