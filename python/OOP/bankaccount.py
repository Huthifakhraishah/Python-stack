class BankAccount:
    def __init__(self,name, int_rate=0.01, balance=0):
        self.int_rate=int_rate
        self.balance=balance
        self.name=name
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
huthifa=BankAccount("huthifa")
huthifa.deposit(1000).deposit(1000).deposit(200).withdraw(900).yield_interest().display_account_info()
nour=BankAccount("nour")
nour.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(900).yield_interest().display_account_info()
