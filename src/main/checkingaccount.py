from bankaccount import Bankaccount

class Checkingaccount(Bankaccount):
    def __init__(self, accountholder, accountnumber, balance):
        super().__init__(accountholder, accountnumber, balance)

    def withdraw(self, amount):
        proposedbalance = self.balance
        if proposedbalance > 0:
            return super.withdraw(amount)
        elif proposedbalance > -100:
            return super.withdraw(amount + 10)
        else:
            return self.balance