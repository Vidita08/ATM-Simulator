class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

def main():
    # Create a bank account
    account_number = "1234567890"  # Replace with a real account number
    pin = "1234"  # Replace with a real PIN
    account = BankAccount(account_number, pin)

    print("Welcome to the ATM")
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            print(f"Balance: ${account.check_balance()}")
        elif choice == "2":
            amount = float(input("Enter the deposit amount: $"))
            print(account.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: $"))
            print(account.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
