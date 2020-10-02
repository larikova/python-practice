name1 = input("Enter your friend's name: ")
name2 = input("Enter your friend's name: ")
name3 = input("Enter your friend's name: ")
friends_list = [name1, name2, name3]
repeat = input("Do you want to add more friends? ")
while repeat == "yes":
    new_friend = friends_list.append(input("Enter a name: "))
    repeat = input("Do you want to add more friends? ")
print("Yoy have", len(friends_list), "people coming to your party")
print(friends_list)
name_del = input("Enter one name from the list: ")
print(name_del, "is in position", friends_list.index(name_del), "on the list")
question = input("Do you still want to invite this friend to the party? ")
if question == "no":
    friends_list.remove(name_del)
print(friends_list)
