import subprocess
import argparse

def run():
    parser = argparse.ArgumentParser(description='Python handle process err')
    parser.add_argument("--file_name", help="String of input file name.",type=str)
    args = parser.parse_args()

    res = subprocess.Popen(["bash", "start.sh", args.file_name], stdout=subprocess.PIPE)
    status = res.wait()
    if status == 0:
        print({'status':status, 'msg':'File {args.file_name} read successfully'})
    elif status == 2:
        print({'status':status, 'msg':'File {args.file_name} is not readable'})
    else:
        print({'status':status, 'msg':'File {args.file_name} is not exist'})

if __name__=='__main__':
    run()