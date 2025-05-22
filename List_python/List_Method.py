basket = [1,2,3,4,5]
print(len(basket)) # 5

#adding methods 
basket.append(100) # add 100 to the end of the list
new_list  = basket 
print(new_list) # [1, 2, 3, 4, 5, 100]
print(basket) # [1, 2, 3, 4, 5, 100]

#insert method 
basket.insert(0, 100) # add 100 to the start of the list
print(basket) # [100, 1, 2, 3, 4, 5, 100]

# removing methods
basket.remove(4) # remove 100 from the list 
print(basket) # [1, 2, 3, 5, 100] 


#clear method
new_list = basket.clear()
print(basket)