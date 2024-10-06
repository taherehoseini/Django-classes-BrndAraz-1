def is_valid_text(char_count):
    def inner_decorator(func):
        def wrapper(name):
            if len(name) <= char_count: 
               return func(name)
            else:
                raise ValueError(f'name length is bigger than {char_count}')   
        return wrapper
    return inner_decorator


@is_valid_text(10)
def user_name(name):
    return name


@is_valid_text(10)
def user_family(family):
    return family


def register(name, family):
    try:
        name = user_name(name)
        family = user_family(family)
        print(f'{name} {family} registerd sucessfuly !!')
    except:
        print('register not sucessfuly !')    

name, family = input().split(',')
register(name, family)        
