import collections
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
import sys
import os

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
    name = command.rsplit('.', 1)
    if len(name) == 2:
        file_name = '{0}_{1}'.format(name[0], name[1])
        content = locals().get(file_name)
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




