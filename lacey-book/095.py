from array import *
import math

nums = array('f', [25.44, 34.23, 61.54, 73.86, 89.22])

tryAgain = True
while tryAgain == True:
    num = int(input("Enter a whole number between 2 and 5: "))
    if num < 2 or num > 5:
        print("Incorrect valid, try again")
    else:
        tryAgain = False
for i in range(0, 5):
    answer = nums[i]/num
    print(round(answer, 2))
