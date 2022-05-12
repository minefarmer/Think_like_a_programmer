

class Account:
    __accNumber = 0
    __balance = 0
    def __init__(self, accNumber, balance = 1000):
        self.setAccNumber(accNumber) # self.__accNumber = accNumber  # the double underscore hides the info
        self.setBalance(balance)
    def getAccountNumber(self):
        return self.__accNumber
    def setAccNumber(self, accNumber):
        if len (accNumber) != 10 or not accNumber.isdigit():  # "1234567890"
            print("Invalid account number!")
        else:
            self.__accNumber = accNumber
    def getBalance(self):
        return self.__balance
    def setBalance(self, amount):
        try:
            if amount >= 0:
                self.__balance = amount
            else:
                raise Exception("Amount should be greater that zero or " "equal to zero")
        except Exception as e:
            print(e.args)
    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount should be positive")
    def debit(self, amount):
        if self.__balance < amount:
            print("amount withdrawn exceeds the current balance")
        else:
            self.__balance -= amount
    def __str__(self):
        return "Account Number: {}, Balance: ".format(self.getAccountNumber(), self.getBalance())
myAccount = Account("123456")
print(myAccount)
print(myAccount.getAccountNumber())
print(myAccount)
print(myAccount.getAccountNumber)
print(myAccount.getBalance())
myAccount.setBalance(2000)
print(myAccount.getBalance())
myAccount.credit(1000)
print(myAccount.getBalance())
myAccount.debit(500)
print(myAccount.getBalance())
myAccount.debit(4000)  # Invalid account number!
                        # Account Number: 0, Balance: 
                        # 0
                        # Account Number: 0, Balance: 
                        # <bound method Account.getAccountNumber of <__main__.Account object at 0x7fb347c3afd0>>
                        # 1000
                        # 2000
                        # 3000
                        # 2500
                        # amount withdrawn exceeds the current balance

myAccount.setBalance(-100)  # Invalid account number!
                            # Account Number: 0, Balance: 
                            # 0
                            # Account Number: 0, Balance: 
                            # <bound method Account.getAccountNumber of <__main__.Account object at 0x7f7901bc9fd0>>
                            # 1000
                            # 2000
                            # 3000
                            # 2500
                            # amount withdrawn exceeds the current balance
                            # ('Amount should be greater that zero or equal to zero',)
                        