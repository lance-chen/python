# Filename: reference.py

print 'Simple Assignment'
shoplist = ['apple', 'mange', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist

print 'Copy by making a full slice'
mylist = shoplist[:]
del mylist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
