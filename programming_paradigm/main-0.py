import sys

from programming_paradigm.bank_account import BankAccount

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: main-0.py [--initial-balance <amount>] <operation> [<amount>]")
        print("Operations: deposit, withdraw, balance")
        print("Example: main-0.py --initial-balance 500 deposit 100")
        sys.exit(1)

    initial_balance = 0
    if sys.argv[1] == "--initial-balance":
        try:
            initial_balance = float(sys.argv[2])
            if initial_balance < 0:
                print("Initial balance cannot be negative.")
                sys.exit(1)
            operation = sys.argv[3].lower()
            amount = 0
            if len(sys.argv) > 4:
                try:
                    amount = float(sys.argv[4])
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
                    sys.exit(1)
        except ValueError:
            print("Invalid initial balance. Please enter a valid number.")
            sys.exit(1)
    else:
        operation = sys.argv[1].lower()
        amount = 0
        if len(sys.argv) > 2:
            try:
                amount = float(sys.argv[2])
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                sys.exit(1)

    if operation not in ["deposit", "withdraw", "balance"]:
        print("Invalid operation. Use deposit, withdraw, or balance.")
        sys.exit(1)

    if operation in ["deposit", "withdraw"] and amount <= 0:
        print("Amount must be greater than zero.")
        sys.exit(1)

    account = BankAccount(initial_balance=initial_balance) # type: ignore

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
        print(f"Current balance: ${account.get_balance():.2f}") # type: ignore

if __name__ == "__main__":
    main()