food_dictionary = {}
food1 = input("Enter a food you like: ")
food_dictionary[1] = food1
food2 = input("Enter another food you like: ")
food_dictionary[2] = food2
food3 = input("Enter a third food you like: ")
food_dictionary[3] = food3
food4 = input("Enter a last food you like: ")
food_dictionary[4] = food4
print(food_dictionary)
dislike = int(input("Wich of these do you want to ger rid off? "))
del food_dictionary[dislike]
print(sorted(food_dictionary.values()))
