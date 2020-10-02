num = [111, 222, 333, 444]
for i in num:
    print(i)
selection = int(input("Enter a number: "))
if selection in num:
    print(selection, "is in positions", num.index(selection))
else:
    print("This is not in the list")

# num = [111, 222, 333, 444]
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# answer = int(input("Enter a number: "))
# if answer == num[0]:
#     print("Position of the number", answer, "is 1")
# elif answer == num[1]:
#     print("Position of the number", answer, "is 2")
# elif answer == num[2]:
#     print("Position of the number", answer, "is 3")
# elif answer == num[3]:
#     print("Position of the number", answer, "is 4")
# else:
#     print("That is not on the list")
