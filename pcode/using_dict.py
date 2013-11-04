# Filename: using_dict.py

ab  = { 'Swaroop' : 'swaroopch@byteofpytho.info',
        'Larry'   : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer' : 'spammer@hotmail.com'
    }

print "Swaroop's address is %s" % ab['Swaroop']

# add a key/value pair
ab['Guide'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print '\n There are %d contacts int the address-book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'Guido' in ab:
    print "\nGuido's address is %s" % ab['Gudio']
