from abc import ABC,abstractmethod

class Account(ABC): 
    balance=0
    def check_balance(self):
        print(f"current balance is, {self.balance}")

    @abstractmethod
    def deposite(self,amount):  
        pass

    @abstractmethod
    def withdrow(self,amount):
        pass

class Saving(Account):

    def deposite(self, amount):
        self.balance +=amount
    
    def withdrow(self, amount):
        if amount>self.balance:
            print("Insuffcient amount")
        else:
            self.balance-=amount
    
class Loan(Account):

    def deposite(self, amount):
        if amount>self.balance:
            k = amount-self.balance
            print(f"load cleared ,  you have left {k}")
            self.balance=0
        else:
            self.balance-=amount
    
    def withdrow(self, amount):
        self.balance+=amount
    

# s = Saving()
# s.check_balance()
# s.deposite(5000)
# s.deposite(10000)
# s.check_balance()
# s.withdrow(150000)
# s.check_balance()

# l = Loan()
# l.check_balance()
# l.withdrow(5000)
# l.check_balance()
# l.deposite(3000)
# l.check_balance()

a = Account()