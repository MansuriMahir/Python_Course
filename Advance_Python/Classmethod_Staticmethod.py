# ClassMethod - It is a method that belongs to a class rather than an object.
# Static Method - It is a method that belongs to a class but doesn't require an instance of the class to operate.

# cls is the shorthand for the class itself.
class player_character:
    membership = True
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    
    def attack(self, target):
        print(f"{self.name} attacks {target} with {self.weapon}")
    @classmethod
    def adding_things(cls,num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def adding_things(num1, num2):
        return  num1 + num2

player1 = player_character("John", 100, "Sword") 
player2 = player_character("Alice", 80, "Axe")

player1.attack(player2.name)

player3 = player_character.adding_things(10, 20)
print(player3)
