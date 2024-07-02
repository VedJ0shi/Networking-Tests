import requests

class MyTokenAuth(requests.auth.AuthBase):

    def __init__(self, token):
        self._token = token

    def __call__(self, request): 
        """Attach an API token to the Authorization header."""
        request.headers['Authorization'] = f'Bearer {self._token}'
        return request

github_personal_access_token = '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'


resp = requests.get(
    "https://api.github.com/user",
    auth = MyTokenAuth(github_personal_access_token) #instance of the auth handler created; will be called during request-setup
)

print(resp)
print(resp.text)

print('Grabbing sent request header info...')
print(resp.request.headers)
print(resp.request.headers.get('Authorization'))