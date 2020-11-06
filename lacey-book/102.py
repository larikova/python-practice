list = {}
for i in range(0, 4):
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    size = int(input("Enter a shoe size: "))
    list[name] = {"Age": age, "Shoe size": size}
ask = input("Enter the name: ")
print(list[ask])
