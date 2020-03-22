def app(environ, start_response):
    data = b'Hello, World!\n'
    status = '200 OK'
    responce_headers = [
	('Content-type', 'text/plain'),
	('Content-Length', str(len(data)))
    ]
    start_responce(status, responce_headers)
    print(environ) 	
    return iter([data])
