from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse


class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        ## sending response header
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()

        response = "Hello World. Am running"

        self.wfile.write(bytes(response, "utf-8"))
        ## python always returns values
        return

def run():
  print('starting server...')

  # Server settings
  # running the server on port 8081
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, myHandler)
  print('running server...')
  httpd.serve_forever()


run()
