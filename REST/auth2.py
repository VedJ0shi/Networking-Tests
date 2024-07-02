import requests

github_personal_access_token = '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'

resp = requests.get(
    "https://api.github.com/user",
    auth = ('',  github_personal_access_token)
)

print(resp)
print(resp.text)

print('Grabbing sent request header info...')
print(resp.request.headers)
print(resp.request.headers.get('Authorization'))