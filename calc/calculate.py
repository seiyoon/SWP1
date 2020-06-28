from cgi import parse_qs
from template import html

def application(environ, start_response):
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
        sum = -1
        product = -1
	string = "Good^^"
	try:
                a, b = int(a), int(b)
                sum = [a + b]
                product = [a * b]
	except ValueError:
		string = "error!"

        response_body = html % {
                'sum' : sum,
                'product' : product,
		'string' : string,
        }
        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [(response_body)]

