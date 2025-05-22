#Range
# Its the most common tool that we get out of the box in python.    
# its is a special types of object that generates a sequence of numbers. 
# it is most commonly used for looping in Python.

print(range(100))

for number in range(100):
    print(number)
    # It will print number from 0 to 100.
    # It was able to loop a 100 times 

for _ in range(10):
    print(_)
    # (_) its a variable where we don't care about the value. It's used when we don't need to use the value in the loop.

for number in range(0,10,2):
    print(number)
    # It will print number from 0 to 10 with step 2.
    # It will print 0, 2, 4, 6, 8.

# for _ in range(0,10,-1): #it will not print any number as it will start from 10 and go down to 0. if ypu want to print do this 
for _ in range(10,0,-1): # It will print number in reverse order 
    print(_) 


# what is range 
# so range create a special kind of object that can iterate over. 


#for convert range to list
for _ in range(10):
    print(list(range(10))) # it will print [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0  


print(list(range(10,0,-1)))
