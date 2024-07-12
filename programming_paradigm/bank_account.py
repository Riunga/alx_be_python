class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        elif amount > self.__account_balance:
            print("Insufficient funds.")
            return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        print(f"Current balance: ${self.__account_balance:.2f}")