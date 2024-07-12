import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: main-0.py <operation> <amount>")
        print("Operations: deposit, withdraw, balance")
        sys.exit(1)

    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else 0

    account = BankAccount(initial_balance=100)  

    if operation == "deposit":
        account.deposit(amount)
    elif operation == "withdraw":
        success = account.withdraw(amount)
        if not success:
            print(f"Could not withdraw ${amount:.2f}")
    elif operation == "balance":
        account.display_balance()
    else:
        print("Invalid operation. Use deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()