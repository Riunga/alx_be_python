class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__account_balance:
            raise ValueError("Insufficient balance")
        self.__account_balance -= amount
        print(f"Withdrew: ${amount:.2f}")  # Print success message

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")