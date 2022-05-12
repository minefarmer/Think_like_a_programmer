

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


bDate = Date(1900, 9, 2)
print(bDate)  # 1900// 0//02

eDate = Date(1993, 2, 29)
print(bDate)  # Invalid Day
              # 1900// 0//02 
