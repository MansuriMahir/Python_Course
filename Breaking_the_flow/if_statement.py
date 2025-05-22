# a = 33 
# b = 210 
# if b > a:
#     print("b is greater than a ") 

# # elif 
# a = 33 
# b = 33 
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print(" a and b are equal")    

#else 
# a = 200
# b = 33 
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print(" a and b are equal")
# else:
#     print("a is greater than b ")  


#Short Hand If ... Else
# a = 2 
# b =  330
# print("A") if a > b else print("B") 

#Short Hand If... else... else
# a = 200
# b = 200 
# print("A") if a > b else print("=") if a == b else print("B") # output: =  as both a and b are equal.

#Test if a is greater than b, AND if c is greater than a: 
#The and keyword is a logical operator, and is used to combine conditional statements:
# a = 200 
# b = 100 
# c = 300 
# if a > b and c > a:
#     print("Both Conditions are True") 


# #Test if a is greater than b, OR if a is greater than c:
# #The or keyword is a logical operator, and is used to combine conditional statements:
# a = 200 
# b = 33 
# c = 500 
# if a > b or a > c:
#     print("At least one of the condition is true")
 

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
# NOT 
# a = 200 
# b = 33 
# if not a > b:
#     print("a is not greater than b")


#Nested If
#You can have if statements inside if statements, this is called nested if statements.

# x = 41

# if x > 10:
#     print("Above 10")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20")


#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 22
c = 11
if a>b:
    pass
