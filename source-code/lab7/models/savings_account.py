from .account import Account

class SavingAccount(Account):
    #override the constructor
    def __init__(self, account_no, owner, balance, interest_rate):
        super().__init__(account_no, owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        self.balance += self.balance* self.interest_rate
        self._add_history("INTEREST",round(self.interest_rate*self.balance,2))