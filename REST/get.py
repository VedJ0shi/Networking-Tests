import requests

url = input('url: ')
if not url:
    url = "https://api.github.com"

resp = requests.get(url)   #returns a requests.models.Response object
print('returned:', type(resp))

if resp.status_code < 400:
    print(f'{resp.status_code}, Success')

elif resp.status_code >= 400: #unlike urlib.request.urlopen(), an exception is not raised for such status codes
    print(f'{resp.status_code}, Failure')

if resp:
    print('Response objects with status codes under 400 evaluate to True')
elif not resp:
    print('Response objects with status codes 400 and above are Falsey')