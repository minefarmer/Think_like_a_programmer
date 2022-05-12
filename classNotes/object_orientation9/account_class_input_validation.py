

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
        if amount >= 0:
            
            self.__balance = amount
        else:
            print("Amount should be greater than zero or equal to zero")
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
myAccount = Account("123456", "1000")
print(myAccount)
print(myAccount.getAccountNumber())
myAccount = Account("123456")
print(myAccount)
print(myAccount.getAccountNumber)
print(myAccount.getBalance())
myAccount.setBalance(2000)
print(myAccount.getBalance())
myAccount.credit(1000)
print(myAccount.getBalance())
myAccount.debit(500)
print(myAccount.getBalance())
myAccount.debit(4000)
print(myAccount.getBalance())
myAccount.debit(500)
print(myAccount.getBalance())
myAccount.balince = -1000     # I am directly accessing the data value
print(myAccount.__balance)
                    # Traceback (most recent call last):
                    # File "/home/carl/Desktop/MatsHub/Think_like_a_programmer/classNotes/object_orientation9/information_hiding.py", line 58, in <module>
                    #     print(myAccount.__balance)
                    # AttributeError: 'Account' object has no attribute '__balance'
