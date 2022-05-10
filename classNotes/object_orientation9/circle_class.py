'''         Circle class

    Circle
radius
color
---------
getRadius()
getColor()
getArea()


'''
import math
class Circle:
    
    def __init__(self, r, c):
        self.radius = r
        self.color = c
    
    def getRadius(self):
        return self.radius
    
    def getColor(self):
        return self.color
    
    def getArea(self):
        return math.pi * math.pow(self.radius, 2)

print("First Circle Object")
c1 = Circle(3.1, "red")
print(c1.getRadius())
print(c1.getColor())
print(c1.getArea())

print("Second Circle Object")
c2 = Circle(4.0, "green")
print(c2.getRadius())
print(c2.getColor())
print(c2.getArea())

        # First Circle Object
        # 3.1
        # red
        # 30.190705400997917
        # Second Circle Object
        # 4.0
        # green
        # 50.26548245743669
