#!/bin/sh
FILE="index.html"
if [-f $FILE]
then
    rm -rf $FILE
else
    curl https://bitbucket.org/bjgiller/evt-tech-challenge/raw/master/evt-web.html >> $FILE
fi

python3 server.py