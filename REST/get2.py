import requests
from requests.exceptions import HTTPError

url = input('url: ')
if not url:
    url = "https://api.github.com"

resp = requests.get(url)
print(resp.status_code)

try:
    resp.raise_for_status() #can force Response object to raise exception for 400+ status codes
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success')



