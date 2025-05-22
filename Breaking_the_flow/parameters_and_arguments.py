#parameters 
#In Python, parameters are variables declared within the parentheses of a function definition.
# parameters allowed as to give arguments to a function.
def say_hello(name='Azhar', age=36):
    print(f'Hello, {name} you are {age} years old')



# Arguments 
# Arguuments are used as the actual values we provide to a function
say_hello('Mahir', 21)# calling the functions 
say_hello('Sally', 110) # calling the function with different arguments
say_hello('John', 30) # calling the function with different arguments



# Default parameters and Keyword Arguments 
# Positional Arguments 
# this all are calles Positional Arguments
say_hello (21, 'Mahir') # changing the order of arguments
say_hello('Sally', 110) 
say_hello('John', 30) 


# Keyword Arguments 
# Keywords arguments allows us to, well not worry about the position.
say_hello(age=21, name='Gautam') # changing the order of arguments
# it will confused while using Default Parameters


# Default Parameters 
say_hello() # calling the function with default arguments
say_hello('Nehal', 21) # calling the function with different arguments
say_hello('Manish')
# it is used when we call in wrong way it will use default arguments.

     