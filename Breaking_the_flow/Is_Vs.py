#is vs ==
print(True == 1)# it will return True because both are equal
print('' == 1)# it will return False because empty string are not equal
print([] == 1)# it will return False because empty list are not equal
print(10 == 10.0)# it will return True because both are equal
print([] == [])# it will return True because both are equal


# == checks the equality or equyality of value 
# is checks the identity or whether two objects are the same object in memory

print(True is True)
print (1 is 1)
print([] is [])
print(10 is 10)
a = [1,2,3]
b = [1,2,3]
# print(a is b)
print(a == b) # it will return True because both lists have same elements in same order