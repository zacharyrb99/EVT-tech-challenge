#!/bin/sh
FILE=index.html

# if test -f $FILE
# then
#     rm -rf $FILE
# fi
[ -f $FILE ] && rm -rf $FILE #shorthand

curl https://bitbucket.org/bjgiller/evt-tech-challenge/raw/master/evt-web.html >> $FILE # gets html from provided URL
python3 server.py # runs server.py and starts web server