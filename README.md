# EVT Tech Challenge
*I decided to _not_ automate the creation of the SSL certificate because I used a self signed certificate. In a production environment, these would be issue by a certificate authority, so there would be no need to manually create them as I have shown below.*

## Python
### Requirements
- Linux (Ubuntu)
- Python3
- OpenSSL

### Set up
1. `cd python`
2. `mkdir certs`
3. ```openssl req -newkey rsa:2048 -nodes -keyout certs/key.pem -x509 -days 365 -out certs/cert.pem -subj "/C=US/ST=Virginia/L=Waterford/O=Enterprise Vision Technologies/OU=Tech Challenge/CN=Zach Boudreaux"```
4. `./server_script.sh`

## Docker
### Requirements
- Linux (Ubuntu)
- Docker

### Set up
1. `cd docker`
2. `mkdir certs`
3. ```openssl req -newkey rsa:2048 -nodes -keyout certs/key.pem -x509 -days 365 -out certs/cert.pem -subj "/C=US/ST=Virginia/L=Waterford/O=Enterprise Vision Technologies/OU=Tech Challenge/CN=Zach Boudreaux"```
4. `./docker_script.sh`