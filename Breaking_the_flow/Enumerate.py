# Enumerte 
# it is same as a range but it is used for a specific purpose
# I means index and value pairs in a dictionary 

for i, char in enumerate('hello world'):
    print(i, char)


for i,char in enumerate([1,2,3,4,5,6]): # for list index start from 0 by default
    print(i , char)


for i, char in enumerate((1,2,3,4,5,6)):# for tuple 
    print(i , char)


for i , char in enumerate(list(range(100))):
    if char == 50:
        print(f'Index of 50 is {i}')