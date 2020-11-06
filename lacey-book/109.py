print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")
selection = int(input("Make a selection 1, 2 or 3: "))
if selection == 1:
    file = open("Subjects.txt", "w")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("Subjects.txt", "r")
    print(file.read())
elif selection == 3:
    file = open("Subjects.txt", "a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subjects.txt", "r")
    print(file.read())
    file.close()
else:
    print("Error")
