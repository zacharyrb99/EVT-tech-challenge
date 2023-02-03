#!/bin/sh
if [-e index.html]
then
    rm -rf index.html
else
    curl https://bitbucket.org/bjgiller/evt-tech-challenge/raw/master/evt-web.html >> index.html
fi

python3 server.py