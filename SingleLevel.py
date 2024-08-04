class Animal:
    def eat(self):
        print("Eating")

    def walk(self):
        print("Walking")

class Dog(Animal):
    def sound(self):
        print("Bark")

    def run(self):
        print("Running")

d1=Dog()
d1.run()
d1.walk()
d1.sound()
d1.eat()
