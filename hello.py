def app(environ, start_response):
    data = '\n'.join.(environ.get('QUERY_STRING').split('&'))
    status = '200 OK'
    responce_headers = [
	('Content-type', 'text/plain'),
	('Content-Length', str(len(data)))
    ]
    start_responce(status, responce_headers)
    return iter([data])
