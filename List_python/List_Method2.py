basket = [1,2,3,1,'i','i',7,'j',9,'mahir','mansuri']  

# in keyword is used to see if an element is in a list 
# it returns true or false 
# it same like boolean but it is not a boolean 
# boolean ia a data type where it check if the value is the same or not and it returns true or false

print('x' in basket)
print('i' in 'hi my name is mahir ')

#count() method 
# it counts the number of times a value appears in a list
# it returns the number of times a value appears in a list 
print(basket.count(1))
print(f'the number of i in the list is {basket.count("i")}')
print(basket[4])