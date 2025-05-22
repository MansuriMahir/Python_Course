# :=  this is a new features 
# there is new syntax := that assign values to variables as part of a larger expression.

a = 'hellooooo'
if ((n := len(a)>10)):
    print(f'too long {n} elements') 

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)