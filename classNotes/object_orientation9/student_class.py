'''         Student class example
    Class is a 3-compartment Box
    
Class name          Student

(Propertied)        name
                    gpa
                    
(Behaviors)         Setgpa()
                    Getgpa()
                    setName()
                    getName()







'''
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def getGpa(self):
        return self.gpa
    def setGpa(self, gpa):
        self.gpa = gpa
    
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
john = Student("John", 3.7)

print(john.getGpa())  # 3.7
john.setGpa(4.0)
print(john.getName())  # John
john.setName("Ali")
print(john.getGpa())  # 4.0
print(john.getName())  # Ali
