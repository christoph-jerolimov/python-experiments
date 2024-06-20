from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
        else:
            self.send_error(404)

httpd = HTTPServer(('localhost', 8080), MyHandler)
httpd.serve_forever()
# httpd.close_request()