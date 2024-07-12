import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: main-0.py <operation> [<amount>]")
        print("Operations: deposit, withdraw, balance")
        sys.exit(1)

    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else 0

    if operation not in ["deposit", "withdraw", "balance"]:
        print("Invalid operation. Use deposit, withdraw, or balance.")
        sys.exit(1)

    try:
        amount = float(sys.argv[2]) if len(sys.argv) > 2 else 0
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        sys.exit(1)

    if operation in ["deposit", "withdraw"] and amount <= 0:
        print("Amount must be greater than zero.")
        sys.exit(1)

    account = BankAccount(initial_balance=100)

    if operation == "deposit":
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}. New balance: ${account.get_balance():.2f}") # type: ignore
    elif operation == "withdraw":
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew ${amount:.2f}. New balance: ${account.get_balance():.2f}") # type: ignore
        else:
            print(f"Could not withdraw ${amount:.2f}. Insufficient funds.")
    elif operation == "balance":
        account.display_balance()

if __name__ == "__main__":
    main()