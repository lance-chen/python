# Filename: objvar.py

class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializing %s)' % self.name

        Person.population += 1

    def __del__(self):
        '''I am leaving.'''
        print '%s says bye.' % self.name

        Person.population -= 1

        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        '''Greeting by the person.

Really, that's all it dose.'''
        print 'Hi, my name is %s.' % self.name

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d person here.' % Person.population

li = Person('li')
li.sayHi()
li.howMany()

liu = Person('liu')
liu.sayHi()
liu.howMany()

li.sayHi()
li.howMany()

print Person.sayHi.__doc__
print Person.__doc__
print li.__doc__
print liu.sayHi.__doc__

del liu
del li


