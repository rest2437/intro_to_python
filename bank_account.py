class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
        self.acc_interst = 0.02

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.amount -= amount
        if(self.amount < 0):
            self.overdraft_fees += 20

    def acc_interst(self, amount):
        if (self.amount < 0):

        return amount


basic_account = BankAccount()

basic_account.deposit(1000)
print('Basic accout has ${}'.format(basic_account.balance))

basic_account.withdrawl(17)
print('Basic accout has ${}'.format(basic_account.balance))

basic
