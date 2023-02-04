import http.server
import ssl
import os

HOST = "localhost"
PORT = 8080
server_address = (HOST, PORT)

if __name__ == "__main__":
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    print("Web Server started on port: %s" % str(PORT))
    print("Access it at https://%s:%s" % (HOST, PORT))
    
    try:
        httpd.socket = ssl.wrap_socket(httpd.socket, 
                                            certfile="certificates/server.pem", 
                                            keyfile="certificates/key.pem", 
                                            server_side=True,
                                            ssl_version=ssl.PROTOCOL_TLS)
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Web server has been stopped.")
    except Exception as e:
        print("Something went wrong.")
        print(e)
        
    try:
        os.remove("index.html")
    except:
        print("index.html doesn't exist")