#Scope 
# what variables dp i have access to?\

# if True:
#      x = 100
# def some_fun():
#     total = 100

# print(x)  


#Scope Rules

a = 5
def parent():
     #a = 10 #while removing this it will print 5
     def confusion():
        return sum
     return confusion()




print(parent())
print(a)
# print(confusion()) 

# 1- start with local scope 
# 2- parent local?
# 3- Global Scope
# 4- Built in Python functions 
