def app(environ, start_response):
    status = '200 OK'
    data = environ['QUERY_STRING'].split("&")
    data = [item+"\r\n" for item in resp]
    response_headers = [
	('Content-type', 'text/plain'),
	('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return resp
