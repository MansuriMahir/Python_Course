# List Slicing 
# string = "Possible"
# #         01234567
# print(string[0::])


amazon_cart = ['notebook', 'mouse', 'keyboard', 'monitor', 'headphones', 'charger'] 
amazon_cart[0] = 'laptop'
 #(this i used for replecing the element at every list index)
new_cart = amazon_cart[0:3]
new_cart = amazon_cart[:]
 # this is used for slicing the list
new_cart[0] = 'gum'
print(new_cart[0:3])
print(amazon_cart[0::2])
print(amazon_cart[::2])
print(amazon_cart[1::2])
print(amazon_cart)