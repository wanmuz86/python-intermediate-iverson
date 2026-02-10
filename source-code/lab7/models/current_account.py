from .account import Account

class CurrentAccount(Account):

    #constructor initialization
    def __init__(self, account_no, owner, balance, overdraft_limit):
        super().__init__(account_no, owner, balance)
        self.overdraft_limit = overdraft_limit

    # method override
    def withdraw(self, amount):
        #overdraft limit , eg 1000
        # which means I can spend until -1000
        if self.balance - amount >= - self.overdraft_limit : 
            self.balance -= amount
            self._add_history("WITHDRAW", amount)
        else:
            print("Overdraft limit exceeded")
            self._add_history("WITHDRAW_FAILED", amount)
    