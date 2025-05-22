#Tuple 
# Tuple is a collection of items which is ordered and unchangeable. In Python tuples are written with round brackets.
#a unlike list that we cant modify it, there are immutable 
my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)# the different us that it is immutable 
# it make easyer to work with data that doesn't change, it make code safe because people cant change it 
new_tuple = my_tuple[1:3]
print(new_tuple)
# we can use tuple to swap two variables

x,y,z, *other = (1,2,3,4,5,6)
print(x)
print(y)
print(z)
print(other) 

# tuple have 2 methods count() and index()
#count() returns the number of times a specified value occurs in a tuple
#index() searches the tuple for a specified value and returns the position of where it was found
my_tuple = (1,2,3,4,5,1)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))