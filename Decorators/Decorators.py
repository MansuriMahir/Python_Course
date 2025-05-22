#Decorators is a key term in pythons 
# It is a function that takes another function as an argument and returns a new function.
# it is arguemt inside the functions 

# def hello():
#     print('helllloooooo');

# greet = hello
# del hello 

# print(greet())  


# calling functions 
# def hello(func):
#     func()

# def greet():
#     print('still here')

# a = hello(greet)

# print(a) # it will print None because hello function is not returning anything.

# # Higher order function HOC
# def greet(func): # that accept another function 
#     func() # this is higher order function 
    #that function inside the parameter another functions 
    # another way higher order function that returns another functions 

# def greet2():
#     def func():
#         return 5 
#     return func 


# map() :- map function is also higher  
# reduce()
# filter() 
# tis all are higher order functions.


# @decorator
# decorators pattern
def my_decorator(func):
    def wrap_func(x , y):
        print('**********')
        func(x, y)
        print('**********')
    return wrap_func 

# @my_decorator
def hello(greeting, emoji =':('):# keywords arguments
    print(greeting, emoji);  

hello('hello') # it will print hello :(. because hello function is not returning anything.

# a = my_decorator(hello)
# hello('hiii', ':)')
 # it will print hiii :). because hello function is now decorated with my_decorator function.

# # @my_decorator
# def bye():
#     print(' see  you soon') 


# hello2 = my_decorator(hello)
# hello2() # reaping my hello function with decorator. in a sigh to get variable 
# we can like this 
# my_decorator(hello)()



# bye()
# hello()# it will print hello world after applying decorator.
# decorator are used to super bost to functions. 


