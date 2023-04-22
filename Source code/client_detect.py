from http.server import BaseHTTPRequestHandler, HTTPServer


class MyRequestHandler(BaseHTTPRequestHandler):
    


    def do_GET(self):

        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "0"
        self.wfile.write(message.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Starting server...\n\n')
    httpd.serve_forever()
