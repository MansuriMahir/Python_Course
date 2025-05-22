# Break, Continue and Pass
# Break statement: Terminates the loop and moves to the next statement 
# Continue statement: Skips the current iteration and moves to the next one
# Pass statement: Does nothing at all, it's used as a placeholder when a statement is required syntactically but you don't want any code to be executed

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
    # break # stops the loop
    # continue # skips the current iteration
    pass # does nothing

i = 0
while i < len(my_list):
    i += 1
    print(my_list[i])
    # # break # stops the loop
    # continue # skips the current iteration 
    pass # does nothing