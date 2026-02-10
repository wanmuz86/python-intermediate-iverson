# Temporary / Small DB to store the class data
import shelve

class Bank:
    def __init__(self):
        # what is this Data type
        # Dictionary - Key - Value
        self.accounts = {}
    
    def add_account(self,account):
        # what is this line?
        # Save it based on the key
        # The key is account_no - value is account info
        self.accounts[account.account_no] = account
    
    def get_account(self,account_no):
        # what is this line?
        # retrieve it based on the key accounts[account_no]
        return self.accounts.get(account_no)
    
    def list_accounts(self):
        print("\n--Account List --")
        # for each account in the dictionary 
        # show the summary
        # For dictionary, arrangement does not matter
        # For List and Tuple , arrangement matter
        for acc in self.accounts.values():
            print(acc.get_summary())

    # methods to save the accounts in DB
    def save_to_db(self, filename="bank_db"):
        # Open the db with the given filename ("bank_db")
        with shelve.open(filename) as db:
            # for each account information in my accounts dictionary
            for acc_no, acc in self.accounts.items():
                # save it using key-value principle
                db[acc_no] = acc

    # methods to load the accounts in DB
    def load_from_db(self, filename="bank_db"):
              # Open the db with the given filename ("bank_db")
        with shelve.open(filename) as db:
             # for item in the database
            for key in db:
                #retrieve it and put it in the dctionary
                self.accounts[key] = db[key]
