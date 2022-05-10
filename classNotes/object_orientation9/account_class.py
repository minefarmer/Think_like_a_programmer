'''         Account class
    Account
__________________
accNumber
balance
__________________
accNumber
balance)
__________________
_init_(accNumber, balance)
getAccNumber()
getBalance
setBalance()
credit()
debit()
__str__()



'''
class Account:
    def __init__(self, accNumber, balance):
        self.accNumber = accNumber
        self.balance = balance
    def getAccountNumber(self):
        return self.accNumber
    def getBalance(self):
        return self.balance
    def setBalance(self, amount):
        self.balance = amount
    def credit(self, amount):
        self.balance += amount  # self.balance = self.balance + amount
    def debit(self, amount):
        if self.balance < amount:
            print("Amount withdrawn esceeds the current balance")
        else:
            self.balance -= amount
    def __init__(self):
        return "Hi.. I am account class.."
myAccount = Account("123456", 1000)
print(myAccount)
print(myAccount.getAccountNumber)
print(myAccount.getBalance())
myAccount.setBalance(2000)
print(myAccount.getBalance())
myAccount.credit(1000)
print(myAccount.getBalance)
myAccount.debit(500)
print(myAccount.getBalance())

