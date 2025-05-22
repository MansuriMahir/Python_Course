from Atm import user, ATM, my_decorator

ADMIN_ACCOUNT = "admin"
ADMIN_PIN = "0000"

class Admin:
    def __init__(self, account, pin):
        self.account = account
        self.pin = pin

    def authenticate(self, entered_pin):
        return self.pin == entered_pin

    @my_decorator
    def view_all_users(self):
        print("\n--- All ATM Users ---")
        for acc_no, acc_obj in user.items():
            print(f"Account No : {acc_no}")
            print(f"Balance    : {acc_obj.balance}")
            print(f"History    : {len(acc_obj.history) - 1} transaction(s)")
            print(f"Last Txn   : {acc_obj.history[-1]}")
            print("-" * 30)

    @my_decorator
    def delete_user(self, acc_no):
        if acc_no in user:
            del user[acc_no]
            print(f"Account {acc_no} deleted successfully.")
        else:
            print("Account not found.")

    @my_decorator
    def reset_pin(self, acc_no, new_pin):
        if acc_no in user:
            user[acc_no].pin = new_pin
            user[acc_no].history.append(f"PIN reset by Admin.")
            print(f"PIN for Account {acc_no} reset successfully.")
        else:
            print("Account not found.")

    @my_decorator
    def reset_balance(self, acc_no, new_balance):
        if acc_no in user:
            user[acc_no].balance = new_balance
            user[acc_no].history.append(f"Balance reset by Admin to {new_balance}")
            print(f"Balance for Account {acc_no} reset successfully.")
        else:
            print("Account not found.")

    @my_decorator
    def view_total_funds(self):
        total = sum(acc.balance for acc in user.values())
        print(f"Total money in ATM System: {total}")
