

class Date:
    
    _day = 0
    _month = 0
    _year = 0
    
    days_per_month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    def __init__(self, y, m, d):
        self.setYear(y)
        self.setMonth(m)
        self.setDay(d)

    def setDay(self, day):
        #  check if day is in corredt range
        if day > 0 and day <= self.days_per_month[self.month]:
            self._day = day
    
    # check for leap year
        elif self._month == 2 and day == 29 and (self._year % 400 == 0 or (self._year % 4 == 0 and self._year % 100 != 0 )):
            self._day = day
        else:
            print("Invalid Day")
    
    
    def setMonth (self, month):
        if month > 0 and month <= 12:
            self.month = month
        else:
            print("Invalid Month")
    
    def setYear(self, year):
        if year >= 1900 and year <= 2020:
            self._year = year
        else:
            print("Invalid Year")
    
    def getDay(self):
        return self._day
    
    def getMonth(self):
        return self._month
    def getYear(self):
        return self._year
    def __str__(self):
        return "{}//{:>2d}//{:0>2d} ".format(self.getYear(), self.getMonth(), self.getDay())





class Student:
    
    
    __name = 0
    __gpa = 0
    __birthDate = 0
    __enrollDate = 0
    
    def __init__(self, name, gpa, birthDate, enrollDate):
        self.__name = name
        self.__gpa = gpa
        self.__birthDate = birthDate
        self.__enrollDate = enrollDate
    
    def getGpa(self):
        return self.gpa
    def setGpa(self, gpa):
        self.gpa = gpa
    def getName(self, name):
        return self.name
    def setName(self, name):
        self.name = name
    def setBirthDate(self, birthDate):
        self.__birthDate = birthDate
    def getBirthDate(self):
        return self.__birthDate
    def getEnrollDate(self, enrollDate):
        return self.__enrollDate
    def __str__(self):
        return "name: {}, GPA: {}, Birth Date: {}, Enroll Date: {}".format(self.getName(), self.getGpa(), self.__birthdate, self.__enrollDate)


bDate = Date(1992, 3, 8)
eDate = Date(2014, 8, 14)

john = Student("John", 3.1, bDate, eDate)

print(john)



# print(john.getGpa())  # 3.7
# john.setGpa(4.0)
# print(john.getName())  # John
# john.setName("Ali")
# print(john.getGpa())  # 4.0
# print(john.getName())  # Ali

# print(bDate)  # 1900// 0//02

# print(bDate)  # Invalid Day
#               # 1900// 0//02 




'''                Example = Student and Date Class
        Student                                                 Date
    name                                                Day
    gpa                                                 Month
    enrollDate                                          year
___|_____________________________________<>____________|_____________
_init_(name, gpa, birthdate, enrollDate)                _init_(day, month, year)
SEtgpa(gpa)                                             setDay(day)
Getgpa()                                                getDay()
setName(name)                                           setMonth(month)
getName()                                               getMonth()
getBirthDate()                                          setYear(Year)
getEnrollDate()                                         get(year)
_str_()                                                 _str_()



'''