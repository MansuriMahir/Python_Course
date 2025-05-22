#Dictionary 
#dict is a keyword in Python that is used to create a dictionary.
# and its also a data structure that stores data in key-value pairs.
# A dictionary is created by placing a comma-separated sequence of key-value pairs within curly braces {}.
# a key is a string for us and a value can be any data type.
dictionary = {
    'a' : [1,2,3],
    'b' : "hello world",
    'c' : True
}
my_list = [ 
    {
    'a' : [1,2,3],
    'b' : "hello world",
    'c' : True
},
{
    'a' : [4,5,6],
    'b' : "hello world",
    'c' : True
}
]
print(my_list[1]['a'])
print(dictionary['a'][2])
