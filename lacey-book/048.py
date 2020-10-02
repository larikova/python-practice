total = 0
repeat = "yes"
while repeat == "yes":
    total = total + 1
    name = input("Enter a name: ")
    print(name, "has now been invited")
    repeat = input("Do you want to invite anyone else to the party ")
print(total, "people will coming to the party")
