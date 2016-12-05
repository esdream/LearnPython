class Animal(object):
    def run():
        print('Animal is running...')

class Dog(Animal):
    def run():
        print('Dog is running...')

class Timer(object):
    def run(self):
        print('start...')

def run_twice(animal):
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Timer())

kurafi = Dog()
ani = Animal()
print(type(kurafi))
print(type(abs))
print(type(None))
print(type(123))
print(type(ani))
print(dir(Timer()))
