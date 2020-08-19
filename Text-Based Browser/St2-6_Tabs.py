import sys
import os

dir_for_file = sys.argv[1]
os.mkdir(dir_for_file)
files = os.listdir(dir_for_file)
while True:
    url = input()
    if url == 'exit':
        break
    try:
        if '.' in url:
            pass
        else:
            raise SyntaxError
    except SyntaxError:
        print('Error: Incorect URL')