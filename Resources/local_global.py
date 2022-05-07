
def fun1(a, b):
    x = a
    y = b
    global x1
    x1 = 30

def fun2(p, q):
    #print(y)
    print(p, q)

x1, x2 = 10, 20
print(x1)
fun1(x1, x2)
print(x1)