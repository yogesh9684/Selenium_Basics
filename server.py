from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

PORT = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/login.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            username = post_data['username'][0]
            password = post_data['password'][0]

            # Since we are accepting any password, we don't need to check it
            self.send_response(200)
            message = f"Login successful! Welcome, {username}."

            self.end_headers()
            self.wfile.write(bytes(message, 'utf-8'))

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print(f"Serving on port {PORT}")
httpd.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os

PORT = 8080

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/login.html'
        elif self.path == '/logout':
            self.path = '/login.html'
            self.send_response(200)
            self.end_headers()
            message = "You have been logged out."
            self.wfile.write(bytes(message, 'utf-8'))
            return
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

            username = post_data['username'][0]
            password = post_data['password'][0]

            # Accept any password
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Home Page</title>
            </head>
            <body>
                <h2>Welcome, {username}!</h2>
                <form method="GET" action="/logout">
                    <button type="submit">Logout</button>
                </form>
            </body>
            </html>
            """
            self.wfile.write(bytes(response, 'utf-8'))

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print(f"Serving on port {PORT}")
httpd.serve_forever()
