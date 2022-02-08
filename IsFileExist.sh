#!/bin/bash
FILE=$1
if test -f "$FILE"; then
    # 檔案存在
    echo "File $FILE exists."
    exit 0
else
    # 檔案不存在
    echo "File $FILE does not exists."
    exit 1
fi