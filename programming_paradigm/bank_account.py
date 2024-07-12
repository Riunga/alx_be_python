class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.__account_balance += amount
        print(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount > self.__account_balance:
            print("Insufficient funds.")
            return
        self.__account_balance -= amount
        print(f"Withdrew: ${amount:.2f}")  # Print success message

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
