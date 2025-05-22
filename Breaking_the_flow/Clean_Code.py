#Clean Code
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
print(is_even(15)) # True
print(is_even(10)) # True


#another way to write the function
def is_odd(num):
    if num % 2 != 0:
        return True
    return False

print(is_odd(15)) # 


#another way to write the function in clean way 
def is_even_clean(num):
    return num % 2 == 0

print(is_even_clean(15)) # True

    
