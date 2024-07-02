import requests

#Search GitHub repositiories for popular Python projects:
url = "https://api.github.com/search/repositories"
resp = requests.get(url, params={'q':'language:python', 'sort':'stars', 'order':'desc'})
print(resp.url)

content = resp.json() #deserialized dict 

popular_repositiories = content['items'] #returns list of dicts
print(popular_repositiories[:3])

for repo in popular_repositiories[:5]:
    print(f'name: {repo["name"]}')
    print(f'description: {repo["description"]}')
    print(f'stars: {repo["stargazers_count"]}')
    print()
