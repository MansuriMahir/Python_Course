#binding of data amd functions 

class player_character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
player1 = player_character('Mahir', 21)
print(player1.name)
print(player1.age)

player2 = {'name': 'ANISH', 'age': 25}
print(player2['name'])
print(player2['age'])
