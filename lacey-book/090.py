from array import *

nums = array('i', [])

while len(nums) < 5:
    num = int(input("Enter a number between 10 and 20: "))
    if num >= 10 and num <= 20:
        nums.append(num)
        print("Thank you")
    else:
        print("Outside the range")

for i in nums:
    print(i)
