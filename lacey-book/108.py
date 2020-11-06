file = open("Names.txt", "a")
newName = input("Enter a new name: ")
file.write(newName + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()
