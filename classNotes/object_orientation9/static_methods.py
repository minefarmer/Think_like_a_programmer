import math         # Noted are at the bottom

class Calculator:
    
    @staticmethod   # Because the static methods are not associated with the object of the class. Therefore in the static methods we don't need (self) to identify which method we are using.
    def add(x1 , x2):
        return x1 + x2
    
    @staticmethod
    def multiply(x1, x2):
        return x1 * x2
    

print(Calculator.add(10, 20))  # 30


'''         Static methods
Static methods are methods that can be called without an object.
The purpose of static methods is ease of use.
All methods of Math class are static in nature.


'''