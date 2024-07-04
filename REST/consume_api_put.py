import requests


api_base_url = 'https://jsonplaceholder.typicode.com'

endpoint = '/todos/10'

api_url = api_base_url + endpoint

resp = requests.get(api_url)
print('before update:', resp.json())
title = resp.json().get('title')
completed = not resp.json().get('completed')

update = {'userID':1, 'title':title, 'completed':completed}
resp = requests.put(api_url, json=update) #PUT updates resource by replacement
print('after update:',resp.json())
