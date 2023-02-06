# EVT Tech Challenge
*I decided to __not__ automate the creation of the SSL certificate because I used a self signed certificate. In a production environment, these would be issued by a certificate authority, so there would be no need to manually create them as I have shown below.*

## Python
This is the more straight-forward solution. I chose to build a simple web server that has a single endpoint. By default, the SimpleHTTPRequestHandler Class in Python serves index.html if it exists, so there was almost no configuration required with this solution. As stated above, the creation of the SSL certificate isn't automated. After you create the certificate the first time, everything else is automated. Once you run `server_script.sh`, you should be able to visit https://localhost:8080 and see the webpage.
### Requirements
- Linux (Ubuntu)
- Python3
- OpenSSL

### Set up SSL certificate (first time)
1. `cd python`
2. `mkdir certs`
3. ```openssl req -newkey rsa:2048 -nodes -keyout certs/key.pem -x509 -days 365 -out certs/cert.pem -subj "/C=US/ST=Virginia/L=Waterford/O=Enterprise Vision Technologies/OU=Tech Challenge/CN=Zach Boudreaux"```

### Entry point for server automation
4. `./server_script.sh`

## Docker
This is the more portable version solution. I chose Docker because of it portability, all you need is the Docker engine downloaded to run the Docker images. Rather than a Python HTTP server, I chose to use a nginx server. This required more configuration compared to the Python web server, but is more similar to a production model. The python web server isn't meant for a production because of its security concerns, but it is very quick to build. The nginx server is more secure out the box, but requires more configuration.
### Requirements
- Linux (Ubuntu)
- Docker

### Set up SSL certificate (first time)
1. `cd docker`
2. `mkdir certs`
3. ```openssl req -newkey rsa:2048 -nodes -keyout certs/key.pem -x509 -days 365 -out certs/cert.pem -subj "/C=US/ST=Virginia/L=Waterford/O=Enterprise Vision Technologies/OU=Tech Challenge/CN=Zach Boudreaux"```

### Entry point for server automation
4. `./docker_script.sh`