# Abstraction 

    # Abstraction is a process of hiding the internal details and showing only the essential features or properties of an object.
    # In Python, abstraction can be achieved using classes and interfaces.

    # Example:
    # Suppose we have a class called "Car" with attributes like make, model, and year.

# Private vs Public Variables

    # In Python, variables can be declared as private or public. Private variables have a double underscore prefix.

    # Example:
    # class Car:
    #     def __init__(self, make, model, year):


class Player_character:
    def __init__(self,_name,_age):
        self._name = str(_name)
        self._age = int(_age)

    def run(self):
        print('run')

    def speak(self):
       return f'my name is {self._name} and I am {self._age} years old'
player1 = Player_character('Mahir', 21)
player1.name = '!!!'
# player1.speak= 'BOOOO!!!'
print(player1.speak())

def run_player(n1, n2):
    n= n1 + n2
    return n
abc = run_player(55, 9)
print(abc)