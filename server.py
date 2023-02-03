import http.server
import socketserver

HOST = "localhost"
PORT = 8080

# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         self.path = "index.html"
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
# Handler = MyHttpRequestHandler

# with socketserver.TCPServer(("", PORT) , Handler) as httpd:
#     print("Web Server running at port: " + str(PORT))
#     httpd.serve_forever()

class MyServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.path = "index.html"

if __name__ == "__main__":
    myWebServer = http.server.HTTPServer((HOST, PORT), MyServer)
    print("Web Server started on port: %s" % str(PORT))
    print("Access it at http://%s:%s" % (HOST, PORT))
    
    try:
        myWebServer.serve_forever()
    except KeyboardInterrupt:
        myWebServer.server_close()
        print("Web server has been stopped.")
    except:
        print("Something went wrong.")