from models.bank import Bank
from models.current_account import CurrentAccount
from models.savings_account import SavingAccount

def menu():
    print("\n=== Mini Bank Menu ===")
    print("1) List accounts")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Show history")
    print("5) Inspect object")
    print("6) Save & Exit")
    # input -> Wait for user's input (no 1-6)
    # strip() -> remove the whitespace
    return input("Choose: ").strip()

#Utility class using the "Introspection" method
# TO investigate the object / for debuggin
def inspect_object(obj):
    print("\n--Object Inspection ---")
    print("Type:",type(obj))
    print("Attributes",vars(obj))

    methods = [
        name for name in dir(obj)
        if callable(getattr(obj, name)) and not name.startswith("__")
    ]
    print("Methods:", methods)

def main():

    # create the bank, load from DB, initialize data if it s not there
    # similar to previous xercise
    bank = Bank()
    bank.load_from_db()

    if not bank.accounts:
        bank.add_account(SavingAccount("S200", "Ali", 200, 0.05))
        bank.add_account(CurrentAccount("C300", "Mira", 50, overdraft_limit=100))

    # While loop
    # As long as I do not exit  , I will run this

    while True:
        # 1) Show the menu and wait for the choice
        choice = menu()

        if choice == "1":
            # list the bank accounts
            bank.list_accounts()

        elif choice == "2":
            # input - retrieve the account no
            acc_no = input("Account no: ").strip()
            # input - retrieve the amount
            amount = float(input("Deposit amount: "))
            acc = bank.get_account(acc_no)
            if acc:
                acc.deposit(amount)
                print("Deposit done.")
            else:
                print("Account not found.")

        elif choice == "3":
            # input - retrieve the account no
            acc_no = input("Account no: ").strip()
            # input - retrieve the withdraw amount
            amount = float(input("Withdraw amount: "))
            acc = bank.get_account(acc_no)
            if acc:
                acc.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            # print history / based on input (acc number)
            acc_no = input("Account no: ").strip()
            acc = bank.get_account(acc_no)
            if acc and hasattr(acc, "print_history"):
                acc.print_history()
            else:
                print("Account not found or history not enabled.")

        elif choice == "5":
            # inspect / based on input (acc number)
            acc_no = input("Account no: ").strip()
            acc = bank.get_account(acc_no)
            if acc:
                inspect_object(acc)
            else:
                print("Account not found.")

        elif choice == "6":
            # break - go out from the whle loop - end the program
            bank.save_to_db()
            print("Saved. Bye!")
            break

        else:
            # default choice, if not in menu, Invalid choice
            print("Invalid choice.")
if __name__ == "__main__":
    main()