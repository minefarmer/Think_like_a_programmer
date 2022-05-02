'''         Collecting intergers together
Write a program that inputs five intergers from the user and stores them in a list. It then displays all values in the list using a loop


'''
intList = []
for i in range (5):
    num = int(input("Enter value: "))
    intList.append(num)


for j in range(5):
    print(intList[j])  # intergers_together.py
                    # Enter value: 10
                    # Enter value: 20
                    # Enter value: 30
                    # Enter value: 40
                    # Enter value: 50
                    # 10
                    # 20
                    # 30
                    # 40
                    

