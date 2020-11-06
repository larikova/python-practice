from array import *
import random

usersNum = array('i', [])
for i in range(0,3):
    nums = int(input("Enter a number: "))
    usersNum.append(nums)

randomNum = array('i', [])
for i in range(0,5):
    num = random.randint(1, 100)
    randomNum.append(num)

long = sorted(randomNum + usersNum)
for i in long:
    print(i)


