from bankaccount import Bankaccount

class Savingsaccount (Bankaccount):
    def __init__(self, accountholder, accountnumber, balance):
        super().__init__(accountholder, accountnumber, balance)

    def withdraw(self, amount):
        proposedbalance = self.balance - amount
        if self.propsedbalance >= 150:
            return super.withdraw(amount)
        else:
            proposedbalance -=2
            if proposedbalance >= 0:
                return super.withdraw(amount + 2)
            else:  #insufficient funds
                return self.balance


