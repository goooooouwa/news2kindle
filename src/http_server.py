from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import sys

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        subprocess.Popen(["python3", "src/news2kindle.py"])
        message = "Sending news ..."
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', int(sys.argv[1])), handler) as server:
    server.serve_forever()