class Cat:      # Notes at bottom of document
    kind = 'Feline'  # class variable shared by all instances
    __name = ""      # Instance Variable belongs to specific object.
                     # It can vary from Object to Object.
    count = 0
    def __init__(self, name):
        self.__name = name
        Cat.count += 1  # insures that everytime I create a new object, it's value will be incremented and each new object will share the same information  == The value of the count
    def getName(self):
        return self.__name
    def getKind(self):
        return self.kind
print("Value of count before objects", Cat.count)  # Therefor I can use the class name to access the static variable "count" 
c1 = Cat("max")
print("Value of count after first object", Cat.count)
print(c1.getName())  # max
print(c1.getKind())  # Feline

c2 = Cat("Oreo")
print("Value of count after second object, Cat.count")
print(c2.getName())  # Oreo
print(c2.getKind())  # Feline

print(c1.count)
print(c2.count)







'''     Class/Static VAriables
Static or class variables are shared by all instances of class
It should be used in situations when all instances of a class need same information.



'''