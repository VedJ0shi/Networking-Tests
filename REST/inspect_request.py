import requests

'''can inspect the sent request and any redirection history by 
accessing the 'request' and 'history' special attributes of the Response object'''

url = 'https://httpbin.org/post'

resp = requests.post(
    url, 
    data={'foo':'bar', 'alice':'bob'},
    headers={'User-agent': 'Mozilla/5.0'})

print(resp.text)

print('Grabbing info about the sent request...')
print(resp.request) #attribute stores a PreparedRequest object
print(resp.request.headers)
print(resp.request.headers['Content-type'])
print(resp.request.headers['User-agent'])
print(resp.request.body)
print()


resp = requests.post(
    url, 
    json={'foo':'bar', 'alice':'bob'},
    headers={'User-agent': 'Mozilla/5.0'})

print(resp.text)

print('Grabbing info about the sent request...')
print(resp.request) #attribute stores a Prepared Request object
print(resp.request.headers)
print(resp.request.headers['Content-type'])
print(resp.request.headers['User-agent'])
print(resp.request.body)
print()


resp = requests.get(
    'http://github.com/', #server will redirect to https://
    headers={'User-agent': 'Mozilla/5.0'})

print(resp.status_code) #this is the status code for the most recent request (after redirect)
print(resp.url)
print(resp.history) 