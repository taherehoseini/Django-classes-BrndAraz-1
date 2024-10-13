# a = [True, False, True, False]
# print(all(a))
# print(any(a))

# a = [0, '', [], 'Ali', 1]
# print(all(a))
# print(any(a))


# price = {
#    'django': 10,
#    'python': 6,
#    'js': 4
# }

# persons = [
#    {'name': 'parham', 'family': 'bn', 'age':23, 'shopCart': ['django']},
#    {'name': 'kia', 'family': 'gr', 'age':21, 'shopCart': []},
#    {'name': 'sara', 'family': 'mn', 'age':28, 'shopCart': []},
#    {'name': 'alex', 'family': 'hs', 'age':32, 'shopCart': ['python', 'js']},
#    {'name': 'maria', 'family': 'lo', 'age':25, 'shopCart': ['django', 'python']},
#    {'name': 'john', 'family': 'doe', 'age':45, 'shopCart': []},
#    {'name': 'emma', 'family': 'ng', 'age':30, 'shopCart': ['js','django', 'python']},
#    {'name': 'liam', 'family': 'sm', 'age':27, 'shopCart': []},
#    {'name': 'noah', 'family': 'jd', 'age':22, 'shopCart': ['js']},
#    {'name': 'ava', 'family': 'pt', 'age':24, 'shopCart': []},
#    {'name': 'oliver', 'family': 'lk', 'age':25, 'shopCart': []},
#    {'name': 'kamelia', 'family': 'bw', 'age':29, 'shopCart': ['python']}
# ]

#3
# print(
#     list(
#         map(
#             lambda x : {'name': x['name'], 'tootal_price': sum([price[i] for i in x['shopCart']])}
#             ,
#             filter(
#                 lambda x : x['shopCart'],
#                 persons
#             )
#         )
#     )
# )

#2
# print(
#     list(
#         map(
#             lambda x :f"{x['name']} {x['family']}"
#             ,
#             filter(
#                 lambda x : x['shopCart'],
#                 persons
#             )
#         )
#     )
# )

#1
# print(
#     all(
#         map(
#             lambda x : x ['shopCart'],
#             persons
#         )
#     )
# )
###################
# def my_decorater(func):
#     def wrapper():
#         print('bye')
#         func()
#     return wrapper 

# @my_decorater
# def say_hello():
#     print('Hello')

# say_hello()

# a = my_decorater(say_hello)
# a()
##########################
# def my_decorater(func):
#     def wrapper(*args, **kwargs):
#         print(f"bye {kwargs['name']} {kwargs['family']} | your age is {kwargs['age']}| your emeil is {kwargs['email']}")
#         func(*args, **kwargs)
#     return wrapper 

# @my_decorater
# def say_hello(*args, **kwargs):
#     print(f"Hello {kwargs['name']} {kwargs['family']} | your age is {kwargs['age']}| your emeil is {kwargs['email']}")

# say_hello(name='ali', family='hoseini',age= 30, email='ali@ho.com')
##############################
# # USERS = None
# USERS =  'ali.hoo@gmail.com'

# def is_login(func):
#     def wrapper():
#         if USERS:
#             func()
#         else:
#             print('ERROR 404')
#     return wrapper

# @is_login
# def profile_page():
#     print('This is a profile page')

# profile_page()        
#######################################
# USERS = None
USERS =  'ali.hoo@gmail.com'

def is_login(show_page):
    def inner_decorator(func):
        def wrapper():
            if show_page:
                if USERS:
                   func()
                else:
                   print('you must login first')
            else:
                print('page not found')
        return wrapper
    return inner_decorator

@is_login(True)
def profile_page():
    print('This is a profile page')

profile_page()        
