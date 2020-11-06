list = {}
for i in range(0, 4):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    size = int(input("Enter a shoe size: "))
    list[name] = {"Age": age, "Shoe size": size}

ask = input("Enter the name of person you want to remove: ")
del list[ask]

for name in list:
    print((name), list[name]["Age"], list[name]["Shoe size"])
