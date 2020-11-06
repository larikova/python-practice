from array import *

nums = array('i', [2, 3, 2, 3, 5])
for i in nums:
    print(i)
print()

num = int(input("Enter a number from this list: "))
if nums.count(num) == 1:
    print(num, "is in this list once")
else:
    print(num, "is in this list", nums.count(num), "times")


