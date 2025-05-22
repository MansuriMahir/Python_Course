# create dictonary with list of dictionaries
dictionary ={
    'name' : "JOhn",
    'email' : "john@example.com",
    'age' : 25,
    'phone' : 1234567890, 
    'address' : "123 Main St, City, Country"
}
my_list = [
    {
    'name' : "JOhn",
    'email' : "john@example.com",
    'age' : 25,
    'phone' : 1234567890, 
    'address' : "123 Main St, City, Country"
    }   
] 
print(my_list) 
print(my_list[0]['age']) 


# clearly demo starte set , tuple, dictonary and differences 
my_set = {1, 2, 3, 4, 5} 
your_set = {4, 5, 6, 7, 8}  
new_Set =  your_set.difference_update(my_set)
# my_set.difference_update(your_set)  
# your_set.difference_update(my_set)
# your_set.intersection(my_set)

# # my_set.difference(your_set)
# # print(my_set)
# print(my_set - your_set)



# my_tuple = (1, 2, 3, 4, 4, 5)
# print('first value at index 0 is', my_tuple[1])
# print(4 in my_tuple)
# print(f"it will show that 4 is  {my_tuple.count(4) }  times in tuple")
# print(my_tuple.index(5))
# print(len(my_tuple))

# # create a dictionary with key-value pairs
my_dict = {
    'name': "mahir",
    'email': "mahir@example.com",
    'age': 25,
    'phone': 1234567890,
    'address': "123 Main St, City, Country"
    
} 
# my_dict.update({'age' : 55})
# print(my_dict)
my_dict['name'] = 'Manusri' 
my_dict['age'] = 55 # replace value of key 'name' for adding new key value pair or update 
print(my_dict)

# print(my_dict['name']) 
# print('a' in my_dict)
# print(my_dict.get('b'))


