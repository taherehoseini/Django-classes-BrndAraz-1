# def sum(*args):
#     res = 0
#     for num in args:
#         res = res + num
#     return res
# print(sum(2, 3, 10, 3, 5))


# def main(*args, **kwargs):
#     return kwargs
# print(main(name = 'Ali', family = 'Hoseini', age = '24', grade = 'diploma', major = ' electricity'))

# def shopcart(email, *args, **kwargs):
#     print(f'---- USER INFO => {email} ----')
#     for k,v in kwargs.items():
#         print(f'{k} : {v}')
#     print(f'Items : {args}')

# shopcart('tamana.1365@yahoo.com', 'item1','item2', 'item3', 'item4', 0, True, name = 'Tahere', family = 'Hoseini', age = 38 )

# print(
#     (lambda num1, num2 : num1 * num2)(10,3)
# )

# print(
#     (lambda *args : sum([num for num in args]))(10,10,7)
# )
# a = [1,2,3,4,5]
# print(list(map(
#         lambda num: num ** 2 ,
#         a
#     )))


# a = [1,2,3,4,5]
# print(list(filter(
#         lambda num: num >= 3 ,
#         a
#     )))


# a = [1,2,3,4,5]
# print( 
#      list(
#             map( 
#         lambda x : x **2 
#         ,
#         filter(
#             lambda x : x >= 3,
#             a 
#         ) 
#     )
#     )
# )

# a = [1,2,3,4,5]
# print(list(map(lambda x:x**2, filter(lambda x: x>=3, a))))

############################################################## setion 2
# a = [True, False, True, False]
# print(all(a))
# print(any(a))

# a = [0, '', [], 'Ali', 1]
# print(all(a))
# print(any(a))


price = {
   'django': 10,
   'python': 6,
   'js': 4
}

persons = [
   {'name': 'parham', 'family': 'bn', 'age':23, 'shopCart': ['django']},
   {'name': 'kia', 'family': 'gr', 'age':21, 'shopCart': []},
   {'name': 'sara', 'family': 'mn', 'age':28, 'shopCart': []},
   {'name': 'alex', 'family': 'hs', 'age':32, 'shopCart': ['python', 'js']},
   {'name': 'maria', 'family': 'lo', 'age':25, 'shopCart': ['django', 'python']},
   {'name': 'john', 'family': 'doe', 'age':45, 'shopCart': []},
   {'name': 'emma', 'family': 'ng', 'age':30, 'shopCart': ['js','django', 'python']},
   {'name': 'liam', 'family': 'sm', 'age':27, 'shopCart': []},
   {'name': 'noah', 'family': 'jd', 'age':22, 'shopCart': ['js']},
   {'name': 'ava', 'family': 'pt', 'age':24, 'shopCart': []},
   {'name': 'oliver', 'family': 'lk', 'age':25, 'shopCart': []},
   {'name': 'kamelia', 'family': 'bw', 'age':29, 'shopCart': ['python']}
]

#3
print(
    list(
        map(
            lambda x : {'name': x['name'], 'tootal_price': sum([price[i] for i in x['shopCart']])}
            ,
            filter(
                lambda x : x['shopCart'],
                persons
            )
        )
    )
)




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