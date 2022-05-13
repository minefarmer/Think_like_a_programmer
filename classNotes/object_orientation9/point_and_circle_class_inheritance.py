
import math
class Point:        # Notes are at the bottom
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
    
    def setX(self, x):
        self._x = x
    def setY(self, y):
        self._y = y
    
    def getX(self, x):
        return self._x
    def getY(self):
        return self._y

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius
    
    def calculateArea(self):
        return math.pi * self.__radius ** 2

# main program
point = Point(10, 20)
circle = Circle(2, 3, 2.7)
print(circle.calculateArea())
print("point members:", point.__dict__)
print("circle members:", circle.__dict__)  # 22.902210444669596
                                    # point members: {'_x': 10, '_y': 20}
                                    # circle members: {'_x': 2, '_y': 3, '_Circle__radius': 2.7}



'''         Point and circle class

    Point
xCord
ycorx ________      \
_int_(xCord, yCord)  \
setX(xCord)           \
setYCord               \            Circle
getX()                  \
getY()                   \  radius
                          |_________________
                          |_init_(xCord, yCord, radius)
                          |Caculatearea()


'''