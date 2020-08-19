# write your code here
import sys
import os
import requests
import collections
def file_save(dir, content, file_name):
    with open('{}/{}'.format(dir, file_name), 'w') as file:
        file.write(content)

def read_file(dir, file_name):
    with open('{}/{}'.format(dir, file_name), 'r') as file:
        content = file.write()
    return content

dir_for_file = sys.argv[1]
try:
    os.mkdir(dir_for_file)
except:
    pass
stack = collections.deque()
prefix = False
while(True):
    command = input()
    if command == 'exit':
        break
    if command == 'back':
        try:
            current_site = stack.pop()
            back_site = stack.pop()
            stack.appendleft(current_site)
            print(back_site)
        except:
            print('Error')
            continue
    prefix =  command.startswith('https://')
    name = command.rsplit('.', 1)
    if len(name) == 2:
        if prefix:
            current_site = '{0}.{1}'.format(name[0], name[1])
        else:
            current_site = 'https://{0}.{1}'.format(name[0], name[1])
        r = requests.get(current_site)
        content = r.text
        if content is None:
            print('Error')
            continue
        else:
            print(content)
        file_save(dir_for_file, content, name[0])
        stack.append(content)
        continue
    elif len(name) == 1:
        try:
            print(read_file(dir_for_file, name[0]))
        except:
            print('Error')
        continue




