#!/bin/bash
FILE=$1
if test -r "$FILE"; then
    echo "File $FILE is readable."
    exit 0
else
    echo "File $FILE is not readable."
    exit 1
fi