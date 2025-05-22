#Return
# in function we have to writte something where we dont write it will show none in output
def sum(num1, num2):
   def another_function(n1, n2):# functoin inside function.
    return n1 + n2 
   return another_function(num1, num2)

# a function should do one thing really well.
# a function return something. 

# total = sum(10,5)
# print(sum(5,total))
 
total = sum(10,20)
print(total)
      
