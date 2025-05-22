#scope - what variables do i have access to?
# non-local keywords is used to refer to this part, this parent local.
def outer():
    x = "local"
    def inner():
        nonlocal x # it is new keyword in python 3.
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

    # it will print nonlocal as it is inside the inner function and it can access nonlocal variable x
outer() 



 

 # why do we need Scope?
