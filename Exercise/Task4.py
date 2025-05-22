# 1. get user input name, age, bloodgroupp, ph number when u take input must get name i will tae uppercase and age nad ph number will take number 
# will only take number and ph number should not goo about 10    and blood group should be in 2 characters make a list of blood group and user can select a bloodgroup from select options 
#if user enter any thing else u must validite the input and ask the user to enter again and create a contact dictonary and store it in a list 

#blood group list 
blood_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']

contact_list = []

def user_name():
    name = input("Enter your name (uppercase): ")
    if name.isalpha():
        return name.upper()
    else:
        print("Invalid name! Please enter only alphabetic characters.")
def user_age():
    age = input("Enter your age (number): ") 
    if age.isdigit():
            return int(age)
    else:
        print("Invalid age! Please enter only numeric characters.")

def phone_number():
    phone = input("Enter your phone number (10 digits): ")
    length = len(phone)
    if length == 10:
        if phone.isdigit():
            return phone_number
    else:
        print("Invalid phone number! Please enter a 10-digit number.") 



def blood_group():
    blood_group = input("Enter your blood group (2 characters): ").upper()
    if blood_group in blood_group:
        return blood_group
    else:
        print("Invaild blood group! please enter a valid blood group from the list")
        print(blood_group)

# get user input



# create contact dictionary

contact_dict = {
    'name': 'name',
    'age': 'age',
    'phone': "phone_number",
    'blood_group': 'blood_group'
}    

# add contact dictionary to the list

contact_list.append(contact_dict)

print(contact_list)

print("Contact added successfully!")
print("Name added successfully!")
print("Age added successfully!")
print("Phone added successfully!") 

while True:
    print("in the loop")
    name = user_name()
    age = user_age()
    blood_group_value = blood_group()
    contact_value = phone_number()
    
    contact_dict = {
    'name': name,
    'age': age,
    'phone': contact_value,
    'blood_group': blood_group_value 
    }
    print(contact_dict)
    








