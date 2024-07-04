import requests


api_base_url = 'https://jsonplaceholder.typicode.com'

endpoint = '/todos/10'

api_url = api_base_url + endpoint

resp = requests.get(api_url)
print('before update:', resp.json())
title = resp.json().get('title')
new_title = title[:10]

update = {'title':new_title}
resp = requests.patch(api_url, json=update) #PATCH updates resource by modifying only those fields set in the sent JSON
print('after update:',resp.json())