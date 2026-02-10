# 1) import the datetime to capture the transaction history
from datetime import datetime

class Account:

    # balance is defaulted to 0 if it is not specified
    def __init__(self, account_no, owner, balance=0.0):
        self.account_no = account_no
        self.owner = owner
        self.balance = balance 
        # 2) initialize the transation history
        self.history = [] # [] -> Empty array
        # 4) Call add_history to log bank account opened at xx xx date, time
        self._add_history("OPEN", balance)

   
    #3) Add a private method add transaction history
    def _add_history(self, action, amount):
        self.history.append({
            "time":datetime.now().isoformat(timespec="seconds"),
            "action":action, # OPEN, WITHDRAW, DEPOSIT, INTEREST, FAILED 
            "amount":float(amount),
            "balance":float(self.balance)
        })

    def deposit(self, amount):
        # Error handling to make sure amount is positive
        if amount > 0:
            # self.balance = self.balance + amount
            self.balance += amount
            # 5 - Log in transaction history
            self._add_history("DEPOSIT", amount)
    
    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            #6 - LOG in transaction history
            self._add_history("WITHDRAW", amount)
        else:
            print("Insufficient funds")
            #7 - LOG in transaction history
            self._add_history("WITHDRAW_FAILED", amount)
    
    def get_summary(self):
        return f"{self.account_no} | {self.owner} | Balance: {self.balance}"
    
    def print_history(self):
        print(f"\n-- Transaction History: {self.account_no} --")
        for h in self.history:
            print(f"{h['time']} | {h['action']} | amount={h['amount']}| balance={h['balance']}")