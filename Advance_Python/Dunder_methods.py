class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name' : 'Yoyo',
            'has_pets' : False

        }


    def __str__(self):
        return f'This toy color is {self.color} and it is {self.age} years old.'
    
    def __len__(self):
        return 5
    
    def __del__(self):
        print('Object deleted')
    
    def __call__(self):
        return('Yess??')
    
    def __getitem__(self, i):
        return self.my_dict[i]
    


        
    

action_figure = Toy('blue', 5)
print(action_figure.__str__()) # dunder method 
print(str(action_figure))
print(len(action_figure)) # dunder method 
# del action_figure # dunder method 
print(action_figure())
print(action_figure['name'])

