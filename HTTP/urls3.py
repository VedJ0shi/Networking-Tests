from urllib.parse import urljoin

#path structure of a web server's resources is similar to that of a POSIX or Windows file system:

top_level = ['abc', 'xyz'] #located in the root resource

host_url = 'http://www.example.com' # 'www.example.com' is hostname

root = host_url + '/' #root resource

print('first request:', root)
print('second request:', urljoin(root, top_level[0]))
print('third request:', urljoin(root, top_level[1]))
print('fourth request:', urljoin(urljoin(root, top_level[1])+'/', '123'))
print('fifth request:', urljoin(urljoin(urljoin(root, top_level[1])+'/', '123')+'/', 'qwerty'))
print('second request:', urljoin(urljoin(urljoin(root, top_level[1])+'/', '123')+'/', '/'+top_level[0]))


