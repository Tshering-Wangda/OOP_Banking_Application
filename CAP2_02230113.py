import random

# Account class definition
class Account:
    # Initialize the account with account number, password, account type, and balance
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = float(balance)

    # Deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Nu.{amount} into account {self.account_number}. New balance: Nu.{self.balance}")

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            print("Short of money")
        else:
            self.balance -= amount
            print(f"Withdrew Nu.{amount} from account {self.account_number}. New balance: Nu.{self.balance}")

    # Send money to another account
    def send_money(self, receiver_account_number, amount):
        if amount > self.balance:
            print("Short of money")
        else:
            receiver_account = self.get_account(receiver_account_number)
            if receiver_account:
                self.balance -= amount
                receiver_account.deposit(amount)
                self.update_account_data(receiver_account)
                print(f"Sent Nu.{amount} to account {receiver_account_number}. New balance: Nu.{self.balance}")
            else:
                print("Receiver account not found")

    # Delete the account
    def delete_account(self):
        with open("accounts.txt", "w") as f:
            for line in line:
                if line.split(",")[0] != str(self.account_number):
                    f.write(line)
        print(f"Account {self.account_number} deleted")

    # Update account data in the file
    @staticmethod
    def update_account_data(updated_account):
        with open("accounts.txt", "r") as f:
            lines = f.readlines()
        with open("accounts.txt", "w") as f:
            for line in lines:
                account_info = line.strip().split(",")
                if account_info[0] == str(updated_account.account_number):
                    f.write(f"{updated_account.account_number},{updated_account.password},{updated_account.account_type},{updated_account.balance}\n")
                else:
                    f.write(line)

    # Static method to get an account by account number
    @staticmethod
    def get_account(account_number):
        with open("accounts.txt", "r") as f:
            for line in f.readlines():
                account_info = line.strip().split(",")
                if account_info[0] == str(account_number):
                    return Account(*account_info)
        return None

# Define a PersonalAccount class that inherits from Account
class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, "Personal", balance)

# Define a BusinessAccount class that inherits from Account
class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, "Business", balance)

# Function to create a new account
def create_account(account_type):
    account_number = random.randint(100000000, 999999999)
    password = str(random.randint(1000, 9999))  # default password for new accounts
    balance = 0
    if account_type == "Personal":
        account = PersonalAccount(account_number, password, balance)
    elif account_type == "Business":
        account = BusinessAccount(account_number, password, balance)
    else:
        print("Invalid account type")
        return
    with open("accounts.txt", "a") as f:
        f.write(f"{account_number},{password},{account.account_type},{balance}\n")
    print(f"Account created! Account number: {account_number}, Password: {password}")

# Function to login to an existing account
def login(account_number, password):
    account = Account.get_account(account_number)
    if account and account.password == password:
        print(f"Logged in to account {account_number}")
        return account
    else:
        print("Invalid account number or password")
        return None

# Main function to handle user interactions
def main():
    while True:
        print("\n1. Create Account")
        print("2. Log in")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            account_type = input("Enter account type (Personal / Business): ")
            create_account(account_type)
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            password = input("Enter password: ")
            account = login(account_number, password)
            if account:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Send Money")
                    print("4. Balance check")
                    print("5. Delete Account")
                    print("6. Log out")
                    choice = input("Choose an option: ")
                    if choice == "1":
                        amount = float(input("Enter amount for deposit: "))
                        account.deposit(amount)
                        Account.update_account_data(account)
                    elif choice == "2":
                        amount = float(input("Enter amount for withdraw: "))
                        account.withdraw(amount)
                        Account.update_account_data(account)
                    elif choice == "3":
                        receiver_account_number = int(input("Enter receiver account number: "))
                        amount = float(input("Enter amount to send: "))
                        account.send_money(receiver_account_number, amount)
                        Account.update_account_data(account)
                    elif choice == "4":
                        print(f"Your balance amount is Nu.{amount}")
                    elif choice == "5":
                        account.delete_account()
                        break
                    elif choice == "6":
                        print("\nLog out successfull")
                        break
                    else:
                        print("Invalid option")
        elif choice == "3":
            print("\nThank you for using the app")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
