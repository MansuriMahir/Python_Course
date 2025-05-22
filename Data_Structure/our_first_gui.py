#execise 

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,1,1,1,0,0],
    [0,0,1,1,1,0,0],
    [0,0,0,1,0,0,0]
] 

for row in picture:
    for pixel in row:
        if pixel == 0:
            print('*', end='')
        else:
            print(' ', end="")     
    print(' ')     


for row in picture:
    for pixel in row:
        if pixel == 1 :
            print('*', end='')
        else:
            print(' ', end="")     
    print(' ')    


# iteratet over picture 
# if -> print ""
# if 1 -> print *