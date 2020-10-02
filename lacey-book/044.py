num = int(input("How many people you want to invite to a party? "))
if num < 10:
    for i in range(1, num + 1):
        name = input("Enter friends' name: ")
        print(name, "has been invited :) ")
else:
    print("Too many people")
