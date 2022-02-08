## Handling Process Status in Python

The folder structure is like below, and you can add a file that can be successfully read and another can’t be.

```bash
.
├── IsFileExist.sh
├── IsFileReadable.sh
├── main.py
└── start.sh
```

The `[IsFileExist.sh](http://IsFileExist.sh)` will check if your file exist or not.

```bash
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
```

The `[IsFileExist.sh](http://IsFileExist.sh)` will check if your is readable or not

```bash
#!/bin/bash
FILE=$1
if test -r "$FILE"; then
    echo "File $FILE is readable."
    exit 0
else
    echo "File $FILE is not readable."
    exit 1
fi
```

Finally, you can run a python script to get different results that depend on the situation of your file.

```powershell
python main.py --file_name={file_name}
```

1. If `file_name` is exist and is also readable.
    
    ```python
    {'status':0, 'msg':'File {file_name} read successfully'}
    ```
    
2. If `file_name` is not exist.
    
    ```python
    {'status':1, 'msg':'File {file_name} is not exist'}
    ```
    
3. If `file_name` is exist but is not readable.
    
    ```python
    {'status':0, 'msg':'File {file_name} is not readable'}
    ```
