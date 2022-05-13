class Calculator:
    
    @staticmethod
    def add(x1 , x2):
        return x1 + x2
    
    @staticmethod
    def multiply(x1, x2):
        return x1 * x2
    
    @staticmethod
    def average(x1, x2, x3=None):
        if x3:
            return (x1 + x2 + x3) / 3.0
        else:
            return (x1 + x2) / 2.0

print(Calculator.average(10, 20, 30))
print(Calculator.average(20, 30))

