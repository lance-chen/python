# Filename: finally.py

import time

try:
    f = file(r'f:\poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Clean up... closed the file'
