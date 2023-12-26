import http.server
import socketserver
from http import HTTPStatus
from datetime import datetime, timezone
from sys import argv


class TCPServer(socketserver.TCPServer):
    allow_reuse_port = True
    allow_reuse_address = True


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            self.wfile.write(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S").encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')


if __name__ == '__main__':
    port = 8080
    if len(argv) == 2:
        port = int(argv[1])
    httpd = TCPServer(('', port), Handler)
    httpd.serve_forever()
