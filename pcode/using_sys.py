# Filename: using_sys.py

from sys import *

print 'The command line arguments are:'
for i in argv:
    print i

print '\n\nThe PYTHONPATH is', path, '\n'
