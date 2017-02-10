class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('running...')

class Dog(Mammal, Runnable):
    pass

d = Dog()
d.run()
