# Error Handling 
# it allowed to handle errors in a program gracefully.
# try block is used to try a block of code for execution
#try is a key word that indicates the start of a try block
# it will handle a error and proceed to the except block  


# while True:
#     try: 
#         age = int(input("Enter your age: "))
#         10/age
#     except ValueError:
#         print("Please enter a number.")
#     except ZeroDivisionError:
#         print("Please enter age higher than 0.")
#     else:
#         print("Thank you :).")
#         break
#     finally:
#         print('im finally done')
# print('end of try block')





# Error Hanlding2
def sum(num1 , num2):
    try:
        return num1 + num2
    #to combine different error in same way 
    except (TypeError, ValueError) as err :
        print(err)
    # except TypeError as err:
        # print("Both inputs must be numbers." + err)
    finally:
        print('im finally done')



print(sum(10, '20'))




#Error Handling3

# while True:
#     try: 
#         age = int(input("Enter your age: "))
#         10/age
#         raise ValueError("hey cut it out") # it is used full while creating library or module for us.
#     except ZeroDivisionError:
#         print("Please enter age higher than 0.")
#         break
#     else:
#         print("Thank you :).")
#         break
#     finally:
#         print('im finally done')
# print('end of try block')

