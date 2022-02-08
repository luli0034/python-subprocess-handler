import subprocess
import argparse

def run():
    parser = argparse.ArgumentParser(description='Python handle process err')
    parser.add_argument("--file_name", help="String of input file name.",type=str)
    args = parser.parse_args()

    res = subprocess.Popen(["bash", "start.sh", args.file_name], stdout=subprocess.PIPE)
    status = res.wait()
    if status == 0:
        print('Success')
    elif status == 2:
        print('Fail is not readable')
    else:
        print('Fail not exist')

if __name__=='__main__':
    run()