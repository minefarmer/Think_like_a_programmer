'''         Binary Search   (No working for me)

Binary search is more efficient and quicker than a linear search.
It can only be appDictionary Search example
Dictionary Search example.


    Pseudocode
1. Start
2. Initialize list data
3. Set LOC = -1
4. Take Key from user
5. Set L = 0 and U = len(DATA) - 1
6. Set MID = (L + U)
7. While L <= U and data[MID] != Key
    1. if Key < DATA[MID]
        1. Set U = MID -1
    2. Otherwise set L = MID - 1
    3. Set MID = (L + U) / 2 (Integer Division)



DATA = [111, 22, 30, 33, 40, 44, 55, 60, 66, 77, 80, 88, 99]

LOC = -1

key = int(input("Please enter the key: "))

L, U = 0, len(DATA) - 1

MID = (L + U) // 2

while L <= U and DATA[MID] != key:
    if key < DATA[MID]:
        U = MID - 1
    else:
        L = MID + 1
    
    Mid = (L + U) // 2
if DATA[MID] == key:
    LOC = MID
    print("Value found at ", LOC)
else:
    print("Sorry, Nothing was found")

'''



# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

# Element is present at index 3


