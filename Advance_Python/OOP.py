#OOP 
  # Object-oriented programming (OOP) is a programming paradigm that organizes software design using objects.   
  # Objects are instances of classes, which have data members (attributes) and methods (functions). 
  # Classes: A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class have.

# class car:
#     pass
# boj1 = car()  # Creating an object of the Car class
# print(type(boj1))  # It will print <class '__main__.car'> which means boj1 is an instance of the Car class.
# print([])


# creating a code 
# __init__ method is a specail method in python that is automaticaly called when an object is called with the name of the class.
# Attrubes are used to store data in an object.

class player_character:
    membership = True
    # Class Object Atrribute
    def __init__(self, name,age):
        if(player_character.membership):
            self.name = name
            self.age = age 
            

    def run(self):
        print('run')
        return 'done'
    
    def shout(self):
        return f'my name is {self.name} and i am {self.age} years old'

player1 = player_character('Mahir', 21)
player2 = player_character('Kishan', 30) 
player2.attack = 100

print(player1.shout())
print(player2.shout())

# help(list)
# print(player2.age )
         

