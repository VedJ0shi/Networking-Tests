import requests


api_base_url = 'https://jsonplaceholder.typicode.com'

endpoint = '/todos'

api_url = api_base_url + endpoint

todo_dict = {'userId': 1, 'title':'Buy milk', 'completed':False}

resp = requests.post(api_url, json=todo_dict)
#equivalently: requests.post(api_url, data=json.dumps(todo_dict), headers={'Content-type':'application/json'})

print(resp.request.headers.get('Content-type'))
print(resp.request.body)
print(resp.headers)
print(resp.json())
