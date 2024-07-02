import requests

#Search GitHub repositiories for popular Python projects:
url = "https://api.github.com/search/repositories"
resp = requests.get(
    url, 
    params={'q':'real python'},
    headers= {'Accept':'application/vnd.github.text-match+json'}) #Accept tells server what response content types are preferred
    #vnd.github.text-match+json is a proprietary GitHub Accept header; response body will be in a special JSON format

content = resp.json()
first_repo = content['items'][0]
print(first_repo['text_matches'][0]['matches'])

