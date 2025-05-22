user_name = input("What is your user name:")
password = input("What is  your password:") 

password_lenght = len(password)
hidden_password = "*" * password_lenght 

print(f' hi {user_name} your password is {hidden_password}, and your password is {password_lenght} characters long') 
