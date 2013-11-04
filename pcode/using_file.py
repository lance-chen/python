# Filename: using_file.py

poem = '''\
To find a work which is fun
Do something you want to do
Be happy
'''

f = file(r'f:\poem.txt', 'w')
f.write(poem)
f.close()

f = file(r'f:\poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,
f.close()
