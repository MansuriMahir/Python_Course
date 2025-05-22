# creating ATm Machne 

from Atm_Admin import Admin, ADMIN_ACCOUNT, ADMIN_PIN

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('\n--------------------')
        result = func(*args, **kwargs)
        print('--------------------\n')
        return result
    return wrap_func 




class ATM:
   
    def __init__(self, account_number,  pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.history = [f"Inital Balance: {balance}"]
    
    def authenticate(self, entered_pin):
        return self.pin == entered_pin
        # if self.pin == entered_pin:
        #     print("Pin Correct!")
        #     return True
        # else:
        #     print("Pin Incorrect!")
        #     return False
    @my_decorator
    def get_balance(self):
        balance = self.balance
        return balance
    
    @my_decorator
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Withdrew: -{amount} | New Balance: {self.balance} ")
            return "Withdrawal Successful!"
        else:
            return "Insufficient Balance!"
    
    @my_decorator
    def deposit(self, amount):
        self.balance += amount
        self. history.append(f"Deposit: +{amount} | New Balance: {self.balance}")
        return "Deposit Successful!"
    
    @my_decorator
    def view_history(self):
        return "\n".join(self.history)
    

@my_decorator   
def make_choice(atm: ATM):
     while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. View Balance History")
        print("5. Exit \n")
    

        choice = input("Enter your choice: ")

        if choice == "1":
            balance = atm.get_balance()
            print(f"your balance : {balance}")
    
        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                print(atm.withdraw(amount))
                balance = atm.get_balance()
                print(f'Your balance : {balance}')
            except ValueError:
                print("Invalid amount. Please enter a number")
    
        elif choice == "3":
            try:
                amount = float(input("Enter deposit amount :"))
                print(atm.deposit(amount))
                balance = atm.get_balance()
                print(f'your balance : {balance}')
            except ValueError:
                print("Inavlid amount. Please enter a number")

        elif choice == "4":
            print(atm.view_history())
    
        elif choice == "5":
            print("thank you for using the ATM")
            break
        else:
            print("Invalid choice. Please try again. ")


user = {
        "1001": ATM("1001", 1234, 1000),
        "1002": ATM("1002", 4321, 1500),
        "1003": ATM("1003", 1111, 500),
        "3001": ATM("3001", 3001, 100)
        }

@my_decorator
def show_user_list():
    if not user:
        print("No user found in the system. ")
        return
    print("\n--- Registered User in ATM ---")
    for acc_no, acc_obj in user.items():
        last_txn = acc_obj.history[-1] if len(acc_obj.history) > 1 else "No transactions yet "
        print(f"Account Number: {acc_no}")
        print(f"Balance       : {acc_obj.balance}")
        print(f"Transaction   : {len(acc_obj.history)-1} ")
        print(f"Last Transaction: {last_txn}")
        print("-" * 30)

def create_account():
    print("\n--- Create New Account ---")
    while True:
        new_acc = input("Enter new Account Number: ")
        if new_acc in user:
            print("Account already exits. try a different number. ")
        else:
            break
    try:
        new_pin = int(input("Set a 4-digit PIN: "))
        init_balance = float(input("Enter inital deposit amount: "))
    except ValueError:
        print("Invalid input! Account creation failed")
        return
    
    user[new_acc] = ATM(new_acc, new_pin, init_balance)
    print(f"Account created successfuly! Account No:{new_acc}")



print("Welcome to the ATM Machine!")

while True:
    print("1. Login as Admin")
    print("2. Login to Exiting Account")
    print("3. Create New Account")
    print("4. View Total Users")
    print("5. View User List with Details")
    print("6. Exit")

    main_Choice = input("Enter your choice: ")

    if main_Choice == "1":
        admin_account = input("Enter Admin Account Name: ")
        if admin_account == ADMIN_ACCOUNT:
            entered_pin = input("Enter admin PIN: ")
            admin = Admin(admin_account, ADMIN_ACCOUNT)
            if admin.authenticate(entered_pin):
                while True:
                    print("\n--- Admin Panel ---")
                    print("1. View All Users")
                    print("2. Delete User")
                    print("3. Reset User PIN")
                    print("4. Reset User Balance")
                    print("5. View Total ATM Funds")
                    print("6. Exit Admin Panel")

                    admin_choice = input("Enter your Choice: ")

    if main_Choice == "2":
        account_number = input("Enter your account Number: ")


        if account_number in user:
            try:
                entered_pin = int(input("Enter your PIN:"))
            except ValueError:
                print("Invalid PIN format.")
                continue
            user_atm = user[account_number]


            if user_atm.authenticate(entered_pin):
                make_choice(user_atm)

            else:
                print("Invalid Pin! Please try again.")

        else:
            print("Account not found. please try again...")
    
    elif main_Choice == "3":
        create_account()
    
    elif main_Choice == "4":
        print(f'\nTotal User in ATM System: {len(user)}')

    elif main_Choice == "5":
        show_user_list()       

    elif main_Choice == "6":
        print("Thank you for using the ATM system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1,2,3, or 4")

