#*args **kwargs

def super_fun(name, *args , i ='hi', **kwargs):
    total = 0
    print(args)
    print(kwargs) 
    for item in args:
        total += item
        print(total , end=' ')   
    for item in kwargs.values():
        total += item 
        print(total)
    
    return sum(args)

print(super_fun('Mahir', 1,2,3,4,5, num1=10, num2=20))


#Rules: params, args, default params, **kwargs