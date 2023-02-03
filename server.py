import http.server
import socketserver
import ssl

HOST = "localhost"
PORT = 80
server_address = (HOST, PORT)

# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.path = "index.html"
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
# Handler = MyHttpRequestHandler

# with socketserver.TCPServer(("", PORT) , Handler) as httpd:
#     print("Web Server running at port: " + str(PORT))
#     httpd.serve_forever()

class MyServer(http.server.SimpleHTTPRequestHandler):
    # Handles GET request
    def do_GET(self):
        self.send_response(200) # Responds with 200 OK status code
        self.send_header("Content-type", "text/html") # Specifies HTTP header, sets media type of resource to html
        self.end_headers()
        self.path = "index.html" # Sets path to HTML file that will be served
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == "__main__":
    web_server = http.server.HTTPServer(("", PORT), MyServer)
    print("Web Server started on port: %s" % str(PORT))
    print("Access it at http://%s:%s" % (HOST, PORT))
    
    try:
        web_server.socket = ssl.wrap_socket(web_server.socket, certfile="server.pem", keyfile="server.key", server_side=True)
        web_server.serve_forever()
    except KeyboardInterrupt:
        web_server.server_close()
        print("Web server has been stopped.")
    except:
        print("Something went wrong.")