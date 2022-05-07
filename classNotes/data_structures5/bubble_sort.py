'''     Bubble Sorting  ( not working for me)



LIST = [12, 43, 21, 9, 54, 23, 6, 87, 67, 55]

N = len(LIST)

print("Before Sorting:" , LIST)
for k in range(1, N):
    for j in range(N = k):
        if LIST[j] > LIST[J + 1]:
            temp = LIST[j]
            LIST[j] = LIST[j+1]
            LIST[j+1] = temp

print("After Sorting: " , LIST)

'''     

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")

# Sorted array is:
#  11  12  22  25  34  64  90 
