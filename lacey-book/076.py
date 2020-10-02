friends_list = []
for i in range(0,3):
    name = input("Enter your name: ")
    friends_list.append(name)
repeat = input("Do you want to add more friends? ")
while repeat == "yes":
    new_friend = friends_list.append(input("Enter a name: "))
    repeat = input("Do you want to add more friends? ")
print("Yoy have", len(friends_list), "people coming to your party")
print(friends_list)
