# class Animal():
#     def make_sound(self):
#         pass


# class Dog(Animal):
#     def make_sound(self): 
#         return 'Bark'


# class Cat(Animal):
#     def make_sound(self): 
#         return 'Meio'



# def animal_sound(animals):
#     for animal in animals:
#         print(animal.make_sound())

# animals = [Dog(), Cat()]

# animal_sound(animals)

###############################################
# from abc import ABC, abstractmethod 

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         ...

#     @abstractmethod    
#     def perimeter(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
      
#     def area(self):
#         return  3.14 * self.radius * self.radius

#     def perimeter(self):
#         return 3.14 * 2 * self.radius   
    


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
      
#     def area(self):
#         return  self.width * self.height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    

# def shape_inf(shapes):
#     for shape in shapes:
#         print(f'Shape : {type(shape).__name__}, Area : {shape.area()}, Perimeter : {shape.perimeter()}')

# shapes = [Circle(5), Rectangle(4,6), Circle(3)]

# shape_inf(shapes)

######################################################
class User:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def full_name(self, phone_number):
        return(f'hello {self.name} {self.family}| {self.age} years old | phone_number : {phone_number}')    



class student(User):
    def __init__(self, name, family, age):
        super().__init__(name, family)
        self.age = age

    def full_name(self, phone_number):
        print('=== run method inside student class ===')
        return super().full_name(phone_number)


s = student('Tahere', 'Hoseini', 37)
       
print(s.name) 
print(s.family) 
print(s.age) 
print(s.full_name('09101569815'))

################################################################ MaJuL
