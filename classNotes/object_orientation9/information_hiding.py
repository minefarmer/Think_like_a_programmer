'''         Information hiding
Information or data is stored within the object
It is hidden from the outside world so we can't access it directly.
It can only be manipulated by the object itself
We only giv access to data using functions/behaviors.

    Example
Ali's name is stored within his brain
We can't access hs name directly
Rather we ask him to tell us his name











'''
class Account:
    def __init__(self, accNumber, balance):
        self.__accNumber = accNumber  # the double underscore hides the info
        self.__balance = balance
    def getAccountNumber(self):
        return self.__accNumber
    def getBalance(self):
        return self.__balance
    def setBalance(self, amount):
        if amount  > 0:
            self.__balance = amount
        else:
            print("Amount should be greater than zero")
    def credit(self, amount):
        self.__balance += amount   # self.balance = self.balance + amount
    def debit(self, amount):
        if self.__balance < amount:
            print("amount withdrawn exceeds the current balance")
        else:
            self.__balance -= amount
    def __str__(self):
        return "Hi..I am account class.."
myAccount = Account("123456", 1000)
print(myAccount)
print(myAccount.getAccountNumber())
myAccount = Account("123456", 1000)
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
