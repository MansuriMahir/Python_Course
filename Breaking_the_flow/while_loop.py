# while Loop 

i = 0

while i < 10:
    print(i)
    i += 1
    # break # break statement is used to stop the loop if a certain condition is met.
else:
    print("Loop completed") 



    # it is infinite loop if we don't put any condition to break it.
    # it will print loop infinitely until you stop it manually.
    # it is not recommended to use while loop for such a task.
    # it is better to use for loop or break statement. 


# for loop eg with while loop 

# for loop 
my_list = [1,2,3,4,5]
for item in my_list:
    print(item) # for loop are simple 

# while loop 
i = 0 # creating a counter variable
while i < len(my_list):
    print(my_list[i])
    i += 1  # incrementing the counter variable in each iteration.
    # while loop are more powerful and flexible than for loop.


# one of the useful way to used while loop  

while True:
    input('Say something: ')
    break 

# while loop and for loop cab be used together to solve complex problems.
while True:
    response = input('Say something: ')
    if (response == 'byy'):
        break
        