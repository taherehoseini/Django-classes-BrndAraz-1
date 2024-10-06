# from test_django import User, student
# from Tools.calculate import calculator
# from Tools.test_django import *
# # import test_django

# s = User()
# s.say_hello()

# c = calculator()
# c.sum(20,50,11)
################################################
# import random as ra
# print(ra.randint(10,50))
############################################################################
from hashlib import sha256
from datetime import datetime

class User:
    def __init__(self, name, family, password : str):
        self.__message = sha256()
        self.__message.update(password.encode())
        self.__name = name
        self.__family = family
        self.__password = self.__message.hexdigest()


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value != '' or value != None:
            self.__name = value
        raise ValueError('Please Enter Name Correctly !!')    


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        if value != '' or value != None:
            self.__family = value
        raise ValueError('Please Enter family Correctly !!')    

    @property
    def password(self):
        return self.__password

    @property
    def full_name(self): 
        return f'{self.name} {self.family}'   



class Application:
    def __init__(self):
        self.users = []

    def Register(self, user : User):
        info = (User.name, user.family)
        
        if info not in [(user['user_info'].name, user['user_info'].family) for user in self.users]:

            self.users.append(
                {
                    'user_info' : user,
                    'date_joind' : datetime.now()
                }
            )
        else:
            raise valueError(f'User {user.full_name} is already registeered !')




app = Application()
a = User('Tahere', 'Hoseini', '123456')
b = User('Parham', 'Baradaran', 'Par3333')

app.Register(a)
app.Register(b)

for user in app.users:
    print(user['user_info'].full_name)

