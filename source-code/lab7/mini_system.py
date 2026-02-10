from models.account import Account
from models.bank import Bank
from models.current_account import CurrentAccount
from models.savings_account import SavingAccount

# a = Account("A100", "Aina", 100)
# a.deposit(50) # 150
# a.withdraw(30) # 120
# print(a.get_summary()) #  A100 | Aina | 120

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
    bank = Bank()
    # Get the saved data from db
    bank.load_from_db()

    #if the db is not there -> first time or you delete the db
    if not bank.accounts:
        # If there is no saved account, create a mock bank account data
        bank.add_account(SavingAccount("S200","Ali",200,0.05))
        # Account No C300, Name = Mira, Starting value =50, Overdraftr limit = 1000
        bank.add_account(CurrentAccount("C300","Mira",50,1000))
    
    # Get Ali's bank
    acc = bank.get_account("S200") 
    acc.deposit(20) # 220 / 251

    #Why do we need this line?
    if hasattr(acc,"apply_interest"):
        acc.apply_interest() #231

    # Retrieve the transacion history
    acc.print_history()

    # Verify that a new file bank_db.db file is created after you run it
    bank.save_to_db()
    bank.list_accounts() # ali account is 231 // 26*

    inspect_object(acc)


if __name__ == "__main__":
    main()