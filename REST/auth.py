import requests

resp = requests.get(
    'https://httpbin.org/basic-auth/user/passwd',
    auth= ('user', 'passwd'), #adds an additional 'Authorization' header
    headers = {'User-agent':'Mozilla/5.0'}
)

print(resp.status_code)
print(resp.headers)
print(resp.headers.get('Content-type'))
print(resp.text)

print('Grabbing sent request header info...')
print(resp.request.headers)
print(resp.request.headers.get('Authorization'))