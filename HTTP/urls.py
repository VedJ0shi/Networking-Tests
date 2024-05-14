from urllib.parse import urlparse, parse_qs
#docs: https://docs.python.org/3/library/urllib.parse.html

info = urlparse("http://docs.python.org:80/3/library/urllib.parse.html?highlight=params#url-parsing")

print(info)
print(info.scheme, info.hostname, info.port, info.path, info.query)
print(info.fragment) #not relevant to HTTP protocol; fragment is an anchor-- tells browser where to jump to in document after it is received in HTTP response

print(parse_qs(info.query)) #returns query portion represented as key-value pairs

print(parse_qs('mode=topographic&pin=Boston&pin=San%20Francisco')) #repeated parameter

