class Animal(object):
    def run(self):
        print('animal is running')

class Dog(Animal):
    def run(self):
        print('doggy is running')

def run_twice(animal):
    animal.run()
    animal.run()


animal = Animal()
run_twice(animal)
dog = Dog()
run_twice(dog)

class Cat(Animal):
    def run(self):
        print('run and jump')
run_twice(Cat())
class ciwei(Animal):
    def eat(self):
        print('can t run but hide')
ciweibao = ciwei()
run_twice(ciweibao)
