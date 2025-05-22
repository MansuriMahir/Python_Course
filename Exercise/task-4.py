blood_group = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']




def user_input():
    while True:
        name = input("Enter your name (uppercase): ")
        if name.isalpha():
            break
        else:
            print("Invalid name! Please enter only alphabetic characters.")
    return print(f"Your name is, {name}!")
def user_age():
    while True:
        age = input("Enter your age (number): ") 
        if age.isdigit():
            return int(age)
        else:
            print("Invalid age! Please enter only numeric characters.")
        return print(f"Your age is, {age}!")

def phone_number():
    while True:
        phone = input("Enter your phone number (10 digits): ")
        length = len(phone)
        if length == 10:
            if phone.isdigit():
                return phone_number
        else:
            print("Invalid phone number! Please enter a 10-digit number.") 
        return print(f"Your phone number is, {phone}!")

#a


name = user_input()
age = user_age()
phone_No = phone_number()
blood_grp = blood_group()

