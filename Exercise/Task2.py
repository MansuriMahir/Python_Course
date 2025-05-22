# assign a variable  it should be a string with the namer of Google and check wether the word O is in there 

name = "Google"
print(f' the name is {name} and the O is there in it: {name.count("o")}') 


#check the value of string 15 and int 15 find out which is a greater and smaller 
# 


# complete password 
user_name = input("Enter yout username:")
password = input("Enter your password:")
password_length = len(password)
hidden_password = "*" * password_length
print(f' hi {user_name} your password is {hidden_password} and your password is {password_length} characters long') 

# type conversion 
#convert the string to int 
a = str(10)
b = int(a)
c = type(b)
print(type(int(str(10)))) 

print(type(str(int(a))))

age = 100
user_age =  age / 10
print(user_age)