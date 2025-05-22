#Iterables
# it is an object or a collection that can be iterated over 
# Iterable can be a list, tuple, string, dictionary, set, etc.
#it is collection of item 
#Iterated --> one by one to check each item to the collection.

user = {
    'name' : 'John',
    'age' : 25,
    'city' : 'New York'
} 
{
   'name' : 'mahir',
    'age' : 25,
    'city' : 'Vadodara',
    'phone' : 1234567890  # add new key-value pair to the dictionary  (dictionary is mutable)
}

user['phone']= 123456789 

# this is shotcut version to print key and value at the same time
# for keys, value in user.items(): 
for item in user.items():
 key, value = item;
 print(key, value)

# for item in user.items():
#     print(item) 

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)
