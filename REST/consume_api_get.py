import requests

api_base_url = 'https://jsonplaceholder.typicode.com'

endpoint = '/todos/1'

api_url = api_base_url + endpoint

resp = requests.get(api_url)

print(resp.request.headers)
print(resp.headers)
print(resp.json())
