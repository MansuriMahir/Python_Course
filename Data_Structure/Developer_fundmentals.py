user = {
    'basket' : [1,2,3,4,5],
    'greet' : "hello world",
    'age' : 55
}


user2 =dict(name='johnjohn')
print(user2)

print(user.get('age', 55))

print('basket' in user) 

print('hello' in user.values()) 

print(user.items()) 
print(user.clear())

user2 = user.copy() 
print(user2)

# print(user.pop('age'))
# print(user)

# print(user.popitem())
# print(user)

print(update := user.update({'age' : 55}))
print(user)