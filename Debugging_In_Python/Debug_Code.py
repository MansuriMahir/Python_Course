# Debugging 
# Linting 
#ide / editors 
# read errors 
# pdb
 
import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(5, 10)

