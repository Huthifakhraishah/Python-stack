class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print(f"{self.name} ",f"Balance = {self.balance} ",f"Intrestre rate = {self.int_rate} ")
        return self
    def yield_interest(self):
        self.balance=self.balance+self.balance*self.int_rate
        return self
class User:
    def __init__(self,name,account):
        self.account= BankAccount()
        self.name=name
    def make_deposite(self,amount):
        self.account.deposit(amount).yield_interest()
        return self
    def make_withdrawal(self,amount):
        self.account.withdraw(amount).yield_interest()
        return self
huthifa=User("huthifa",1)
huthifa.make_deposite(1000).make_deposite(1000).make_deposite(1000).make_withdrawal(100)
print(f"His name is {huthifa.name} and he has {huthifa.account.balance} $$ in his bank")
layth=User("layth",2)
layth.make_deposite(1000).make_deposite(1000).make_withdrawal(100)
print(f"His name is {layth.name} and he has {layth.account.balance} $ in his bank")
lana=User("lana",3)
lana.make_deposite(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)
print(f"Her name is {lana.name} and she has {lana.account.balance} $ in her bank")


