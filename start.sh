#!/bin/bash
FILE=$1
bash IsFileExist.sh $FILE
if test $? -eq 0; then
    bash IsFileReadable.sh $FILE
    if test $? -eq 0; then
        exit 0
    else
        exit 2
    fi

fi
exit 1

