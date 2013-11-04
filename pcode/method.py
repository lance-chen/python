# Filename: method.py

class Person:
    def __init__(self, name):
        self.name = name
        print 'init function is running'
    def sayHi(self):
        print 'Hello, how are you?'
        print 'My name is', self.name

p = Person('Chen')
p.sayHi()
print p
