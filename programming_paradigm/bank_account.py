class BankAccount:
    def __init__(self, initial_balance=0):
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number")
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${int(amount):.0f}")  # Truncate the decimal part
        else:
            print("Deposit amount must be a positive number")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be a positive number")

    def display_balance(self):
        if isinstance(self.__account_balance, (int, float)):
            print(f"Current Balance: ${self.__account_balance:.2f}")
        else:
            print("Balance is not a number")