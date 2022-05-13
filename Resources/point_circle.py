
import math
class Point:
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y

    def getX(self):
        return self._x
    def getY(self):
        return self._y

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.__radius = radius

    def calculateArea(self):
        return math.pi * self.__radius ** 2

#main program
point = Point(10, 20)
circle = Circle(2, 3, 2.7)
print(circle.calculateArea())
print("point members:", point.__dict__)
print("circle members:", circle.__dict__)




