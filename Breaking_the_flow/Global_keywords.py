# Scope - What Variables do i have access to?

# a = 10
# def confusion(b):
#     print(b)
#     a = 90

# confusion(300)

total = 0
def increment(total): 
    total += 5
    return total

print(5)

increment(total)
increment(total)
print(increment(increment(increment(total))))




#1- start with local 
#2- parent local?
#3- global?
#4- built-in python?
