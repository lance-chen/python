# Filename: pickling.py

import cPickle as p
#import Pickle as p

shoplistfile = r'f:\shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = file(shoplistfile, 'w')
p.dump(shoplist, f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
