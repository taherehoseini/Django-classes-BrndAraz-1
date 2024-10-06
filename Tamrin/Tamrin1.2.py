li = ['a', 'e', 'i', 'o', 'u']

def name(*args):
    for n in args: 
        print(len(
            list(
                filter(
                        lambda x : x in li , 
                        n
                    
                )
            )
        ))
     
 
user_input = input()
names = user_input.split(' ')
name(*names)

