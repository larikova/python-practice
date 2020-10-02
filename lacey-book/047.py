num1 = int(input("Enter first number: "))
total = num1
answer = "yes"
while answer == "yes":
    num2 = int(input("Enter your number: "))
    total = total + num2
    answer = input("Do you want to add another number? ")
print("Total is ", total)
