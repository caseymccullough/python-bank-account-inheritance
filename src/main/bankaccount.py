class Bankaccount:
    def __init__(self, accountHolderName, accountNumber, balance = 0):
        self.accountHolderName = accountHolderName
        self.accountNumber = accountNumber
        self.balance = balance

    # Function to deposit amount
    def deposit (self, amount):
        self.balance += amount

    #Function to withdraw amount
    def withdraw (self, amount):
        self.balance -= amount

    def __str__(self):
        # return self.accountHolderName, " account, with account number", self.accountNumber, " holds $", self.balance
        result = '%s account #: %i Balance: $%f' % (self.accountHolderName, self.accountNumber, self.balance)
        return result