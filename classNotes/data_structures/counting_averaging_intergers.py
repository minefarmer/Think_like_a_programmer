'''     Find sim and average

Modify the previous proram so that it can find the sum and average of all intergers in a list


'''

intList = []
for i in range(5):
    intList.append(int(input("Enter Value: ")))


sum = 0

for j in range(5):
    sum = sum + intList[j]

print("Sum is ", sum)
print("Average is ", sum/5) # Enter Value: 10
                            # Enter Value: 20
                            # Enter Value: 30
                            # Enter Value: 40
                            # Enter Value: 50
                            # Sum is  150
                            # Average is  30.0
                            

