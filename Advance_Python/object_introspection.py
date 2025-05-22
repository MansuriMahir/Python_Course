#object Interospection


class User:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do Nothing')

class wizard(User):
    def __init__(self,name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
        self.email = email

    def attack(self):
       # calling parent class method
        print(f'attacking with power of {self.power} ')

class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows : arrows left-{self.num_arrows}')
    

#intropection 
wizard1 = wizard('Nehal', 100, 'wizard@example.com')
print(dir(wizard1))


archer1 = Archer('Tony', 200)

# wizard1.sign_in()
# archer1.sign_in()

# print(wizard1.attack())
# print(archer1.attcak())

# def player_attack(char):
#     char.attack()

# player_attack(wizard1)

# player_attack(archer1)


# for char in [wizard1, archer1]:
#     char.attack()


# print(wizard1.email)
