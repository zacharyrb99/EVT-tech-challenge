import http.server
import socketserver

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = "index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT) , Handler) as httpd:
    print("Web Server running at port: " + str(PORT))
    httpd.serve_forever()