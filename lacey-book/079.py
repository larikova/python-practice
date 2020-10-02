nums = []
count = 0
while count < 3:
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    count = count + 1
last_num = input("Do you want to save the last number? ")
if last_num == "no":
    nums.remove(num)
print(nums)
