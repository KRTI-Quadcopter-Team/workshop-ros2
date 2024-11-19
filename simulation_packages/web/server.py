import http.server
import socketserver
from functools import partial

port = 5050
root = "./"

handler = partial(http.server.SimpleHTTPRequestHandler, directory=root)

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Running server on port {port}")
    httpd.serve_forever()