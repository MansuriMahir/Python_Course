#sets methods
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8}

# .difference() it find different elements in two sets
#duplicate elements will be removed
# print(my_set.difference(your_set))


# .discard() it will remove the element from the set
# print(my_set.discard(your_set))
# # print(my_set.discard(5))  # Discarding an element (does not raise an error if the element is not found)
# print(my_set)

# .difference_update() it will remove the elements from the set
# my_set.difference_update(your_set)
# print(my_set)  # Updating the set with the difference of two sets

 
# .intersection() it will find the common elements in two sets
# print(my_set.intersection(your_set))  # Finding the intersection of two sets


# .isdisjoint() it will check if two sets have no elements in common if they have common element it will show false 
# print(my_set.isdisjoint(your_set))  # Checking if two sets are disjoint (no common elements)


# .issubset() it will check if one set is a subset of another set if it has all elements of the other set
# my_set = {4,5}
# your_set = {4,5,6,7,8}
# print(my_set.issubset(your_set))  # Checking if one set is a subset of another set


# .issuperset() it will check if one set is a superset of another set if it has all elements of the other set
my_set = {4,5}
your_set = {4,5,6,7,8}
print(my_set.issuperset(your_set))  # Checking if one set is a superset of another set
print(your_set.issuperset(my_set))  # Checking if one set is a superset of another set

# .union() it will find the union of two sets and it will remove the duplicate elements and it will show the unique elements
# print(my_set.union(your_set))