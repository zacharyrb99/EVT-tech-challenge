#!/bin/bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t webserver .
docker run -d -p 8080:443 -p 8000:80 --name evt-webserver webserver