#Sets 
#sets are unordered collections of unique elements. They are mutable, meaning you can add or remove elements, but they do not support indexing or slicing like lists or tuples. Sets are useful for membership testing and eliminating duplicate entries.
# A set is created by placing all the items (elements) inside curly braces {}, separated by commas.
#set dont allow duplicates
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
my_set = {1, 2, 3, 4, 5}
my_set.add(100)  # Adding an element to the set
my_set.add(2) # Adding a duplicate element (will not change the set) it will not add it again 
print(my_set)

#for eg if we have a array of numbers and we want to remove duplicates
my_list = [1, 2, 3, 4, 5, 1, 2, 3]
print(set(my_list))  # Converting list to set to remove duplicates
# A set can also be created using the set() constructor

print(1 in my_set)  # Checking membership
print(len(my_set))  # Length of the set/ checking length of the set/ it will count the unique elements
print(list(my_set))  # Converting set to list

my_set = {1, 2, 3, 4, 5}
new_set = my_set.copy()  # Copying a set
my_set.clear()  # Clearing a set
print(new_set)
