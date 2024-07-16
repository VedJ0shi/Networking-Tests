from app_views import *
import urllib.parse


#simulates a simple app that renders HTML:
def application(environ, start_response):

    if environ['PATH_INFO'] == '/':
        if environ['REQUEST_METHOD'] != 'GET' or environ['QUERY_STRING']:
            start_response('400 Bad Request', [('Content-Type', 'text/plain'), ('Content-Length', '31')])
            return ['Error: Front Page is not a form']
        page = view1()
        start_response('200 OK', [('Content-Type', 'text/html'), ('Content-Length', f'{len(*page) + 58}')])
        return ['<html><head><title>wsgi_app.py</title></head><body>', *page, '</body>']

    elif environ['PATH_INFO'] == '/users':
        if environ['REQUEST_METHOD'] == 'GET':
            page = view2()
            length = sum(len(line) for line in page)
            start_response('200 OK', [('Content-Type', 'text/html'), ('Content-Length', f'{length + 58}')])
            return ['<html><head><title>wsgi_app.py</title></head><body>', *page, '</body>' ]
        elif environ['REQUEST_METHOD'] == 'POST':
            if environ['QUERY_STRING'] or not int(environ['CONTENT-LENGTH']) > 0 or environ['CONTENT-TYPE'].strip() != 'application/x-www-form-urlencoded':
                start_response('400 Bad Request', [('Content-Type', 'text/plain'), ('Content-Length', '30')])
                return ['Error: Invalid form submission']
            post_body = environ['wsgi.input'].read()
            submission = urllib.parse.parse_qs(post_body)
            new_user = (*submission.get('username'), *submission.get('email'))
            page = view2(create=True, user=new_user)
            length = sum(len(line) for line in page)
            start_response('201 Created', [('Content-Type', 'text/html'), ('Content-Length', f'{length + 58}')])
            return ['<html><head><title>wsgi_app.py</title></head><body>', *page, '</body>' ] 

    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain'), ('Content-Length', '16')])
        return ['URL is not valid']
        
