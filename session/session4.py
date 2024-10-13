# class car():
#     numbrs_of_doors = 4

#     def start(self):
#         print('car started 2!')


# class Benz(car):
#    def say_hello(self, name):
#        return f'hello {name}'

# a = car()
# a.start()

# b = Benz()
# b.start()
# print(b.say_hello('Benz'))
###################################################
class Animal:
    def __init__(self, name):
        self.name = name
       

    def speak(self):
        return 'Anima Sound'
    
    
class Cat(Animal):
     pass     

my_cat = Cat('Alex')
print(my_cat.name)
print(my_cat.speak())