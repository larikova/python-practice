question = input("Which direction the user wants to count (up or down)?: ")
if question == "up":
    num = int(input("Enter the top number: "))
    for i in range(1, num + 1):
        print(i)
elif question == "down":
    num = int(input("Enter the number below 20: "))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don’t understand")
