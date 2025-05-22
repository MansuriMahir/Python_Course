# Multiple Inhertiance 
class USer():
    def sign_in(self):
        print('Logged in')

class Wizard(USer):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power} ') 

    
class Archery(USer):
     def __init__(self, name, arrows):
         self.name = name
         self.arrows = arrows
     
     def Check_Arrows(self):
        print(f'Arrows left : {self.arrows}')
        
     def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archery):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archery.__init__(self, name, arrows)

hybrid = HybridBorg('Borg', 1000 , 250) 
print(hybrid.run())
print(hybrid.attack())
print(hybrid.Check_Arrows())
print(hybrid.sign_in())


