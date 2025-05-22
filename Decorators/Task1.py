# def create_decorators(func):
#     def wrapper_func():
#         print(' ')
#         func()
#         print(' ')
#     return wrapper_func

# @create_decorators
# def user_name():  
    
#     name = input('Enter your name: ')
#     return f'Your name is:{name}'

# user_name() 

def create_decorators(func):
    def user_input():
        print('Enter your below details:')
        result =func()
        print('-----------------------')
        return result , 'Data entered successfully'
    return user_input

@create_decorators
def user_name():
    u_name = input('name :')
    return u_name

@create_decorators
def user_age():
    u_age = int(input('age:'))
    return u_age

# print(user_name())
# print(user_age())

phone_no = input('phone number:')
print(f'Your phone number is: {phone_no}')