import requests

url = 'https://httpbin.org/post' #responds with info about the request

print('sending POST request with HTML form data:')
resp = requests.post(url, data={'foo':'bar', 'alice':'bob'})
print(resp.text)
content = resp.json()
#inspecting the body of the response:
print(content.get('form'))
print(content.get('headers').get('Content-Type') == 'application/x-www-form-urlencoded')
print()

print('sending POST request with JSON data:')
resp = requests.post(url, json={'foo':'bar', 'alice':'bob'})
print(resp.text)
content = resp.json()
#inspecting the body of the response:
print(content.get('form')) #empty 
print(content.get('data'))
print(content.get('headers').get('Content-Type') == 'application/json')

