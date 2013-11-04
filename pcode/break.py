# Filename: break.py

while True:
    s = raw_input('Enter someting : ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
else:
    print 'while stop by break'
print 'Done'
