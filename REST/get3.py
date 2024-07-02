import requests
import json

url = "https://api.github.com"

resp = requests.get(url)

print('body of HTTP response:')
print(resp.text) #guesses bytes encoding scheme based on response headers
print(type(resp.text)) #str (of serialized JSON content)

json_dict = json.loads(resp.text) #deserialize
print(json_dict)
print(type(json_dict)) #dict
print(json_dict.keys())

print(resp.json() == json_dict) #can directly return deserialized body content from the Response object

print('headers of HTTP response:')
print(resp.headers)
print(resp.headers['Server'])
print(resp.headers['Content-type'])
print(resp.headers['Content-length'])

