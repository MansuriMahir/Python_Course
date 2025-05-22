# Inheritance 
# it allow new Object take on the properties and existing objects.
# so it inherts classes attributes and methods.
# in this we have parent class (User) and child class (wizard, Archer) we can say class and subclass.

class User:
    def sign_in(self):
        print('Logged in')

class wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power} ')

class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attcak(self):
        print(f'attacking with arrows : arrows left-{self.num_arrows}')
    


wizard1 = wizard('Nehal', 100)
print(isinstance(wizard1, User))

archer1 = Archer('Tony', 100)

# wizard1.sign_in()
# archer1.sign_in()

# wizard1.attack()
# archer1.attcak()



