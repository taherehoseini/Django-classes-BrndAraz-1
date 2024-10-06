class Animal:
    def __init__(self):
        pass

    def make_sound(self):
        print('Some generic sound')


class Dog(Animal):
    def make_sound(self):
        print('Woof')

class Cat(Animal):
    def make_sound(self):
        print('Meow')

def animal_sound(animal):     
    animal.make_sound()  
    
animals = [Dog(), Cat(), Cat()]

for animal in animals:
    animal_sound(animal)


