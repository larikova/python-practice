from array import *

nums = array('i', [])

for i in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)
nums = sorted(nums)
print(nums)

selectedNums = array('i', [])
selected = int(input("Select one of the numbers: "))
selectedNums.append(selected)
nums.remove(selected)
print("First list: ")
for i in nums:
    print(i)
print("Second list: ")
for i in selectedNums:
    print(i)
