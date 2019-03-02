class BankAccount:
    def __init__(self, account, bank_status= True, amount= 100, balance=0):
        self.balance=balance
        self.account = account
        self.amount = amount
        self.bank_status =bank_status
      
    
    def open(self,account):
        return self.account

    def get_balance(self):
        return self.balance
     
    def deposit(self,amount):
        self.balance +=amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return("choose less amount")
        self.balance -=amount
        return self.balance 

    def close(self):
        self.bank_status=False
