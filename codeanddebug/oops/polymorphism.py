class Animal:
    def sound(self):
        print("animal voice")


class Dog(Animal):
    def sound(self):
        print("bhw bhw")


class Cat(Animal):
    def sound(self):
        print("meow meow")


obj = Dog()
obj.sound()
