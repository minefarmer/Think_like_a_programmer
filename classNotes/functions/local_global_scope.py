'''         Local and global scope
    Points to ponder
local variable cannot be accessed outside the body of the function

Global variables can be accesses anywhere in the program. They can also be accessed within the functions

If the values of global variables are modified within the functions, then they become the local variables of these functions.

Local variables of one function cannot be accessed in the other functions.

If we want to make changes in the global variable within the functions, then we have to use the key wod global to force the scope of that variable as global.




'''
def fun1(a, b):
    x = a
    y = b
    global x1
    x1 = 30
    
def fun2(p, q):
    print(y)
    print(p, q)

x1, x2 = 10, 20
print(x1)  # 10
fun1(x1, x2)
print(x1)  # 30
