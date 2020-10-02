total = int(0)
for i in range(5):
    num = int(input("Enter a number: "))
    question = input("Do you want to include this number? ")
    if question == "yes":
        total = total + num
        print(total)
    else:
        question == "no"
        print(total)
print("Total:", total)
