#!/bin/sh
FILE=index.html
[ -f $FILE ] && rm -rf $FILE
# if test -f $FILE
# then
#     echo "EXISTS"
#     rm -rf $FILE
# fi

curl https://bitbucket.org/bjgiller/evt-tech-challenge/raw/master/evt-web.html >> $FILE
python3 server.py