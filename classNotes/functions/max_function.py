"""         Max() Function
Write a program that can take two numbers from user and then pass these numbers as arguments to  function called max(a, b) where a is the first number and b is the second number. This finction should print the maximum number. 







"""
def Max(a, b):  # He used 'M' capital in Max() because there is a built-in function called max() so Max(). So Max() and max() are differient!
    if a> b:
        print(a, "is the maximum number")
    else:
        print(b, "is the maximum number")

# main program starts here
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("maximum value is", Max(num1, num2))  # Enter number 1: 12
                                    # Enter number 2: 8
                                    # 12 is the maximum number
                                    # maximum value is None
                                        