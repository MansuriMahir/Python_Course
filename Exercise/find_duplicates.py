#Exercise: Check for dupplicates in List:
#append:- The append() method in Python adds a single element to the end of a list
# It modifies the original list in place and does not return a new list

some_list = ['a', 'b', 'b','c', 'd', 'a','e','e']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:  # avoid duplicates and show only first occurrence
            duplicates.append(value)
print(duplicates)