class BankAcoount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposite(self,ammount):
        self.balance = self.balance + ammount
        print(self.balance)
    def withdraw(self,amm):
        if self.balance < amm:
            print("Insufficient funds!")
        else:
            self.balance = self.balance - amm
            print(self.balance)
    def info(self):
        print(f"The owner of the account is {self.owner} having balance {self.balance}")

b1 = BankAcoount("Om",100)

b1.deposite(200)
b1.withdraw(300)
b1.info()

