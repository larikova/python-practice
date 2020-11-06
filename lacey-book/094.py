from array import *

nums = array('i', [1, 2, 3, 4, 5])
for i in nums:
    print(i)
num = int(input("Select one of the numbers: "))

again = True
while again == True:
    if num in nums:
        print("Position of ", num, "is", nums.index(num))
        again = False
    else:
        print("Not in array")
        num = int(input("Try again: "))
