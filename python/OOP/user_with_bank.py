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
    def accountnum(self,num):
        self.balance=self.balance+self.balance*self.int_rate
        self.num=num
        return self
class User:
    def __init__(self,name,account):
        self.account= BankAccount()
        self.name=name
    def make_deposite(self,amount,num):
        self.account.deposit(amount).accountnum(num)
        return self
    def make_withdrawal(self,amount,num):
        self.account.withdraw(amount).accountnum(num)
        return self
huthifa=User("huthifa")
huthifa.make_deposite(1000,1).make_deposite(1000,1).make_deposite(1000,1).make_withdrawal(100,1)
print(f"His name is {huthifa.name} and he has {huthifa.account.balance} $$ in his bank acount {huthifa.account.num} ")
huthifa.make_deposite(100,2).make_deposite(200,2).make_deposite(100,2).make_withdrawal(100,2)
print(f"His name is {huthifa.name} and he has {huthifa.account.balance} $$ in his bank acount {huthifa.account.num} ")


