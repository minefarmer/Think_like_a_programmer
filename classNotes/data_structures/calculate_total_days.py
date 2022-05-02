'''     Calculate Total Days 
Write a program that inputs current day and month from user. It then calculates and displays the total number of days in current year till the entered date
    Assumption: February has 28 days
        Enter Month Number: 6
        Enter Day Number: 3
        Total Number of days till date = 154

'''
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = int(input("Please enter the month: "))  # 6
day = int (input("Please enter the day: "))  # 5

total = day

for i in range(month - 1):
    total = total + days[i]

print("Total days till the entered day/month is ", total)   # Total days till the entered day/month is  156
