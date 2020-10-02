titles = ["How to make a breakfast", "News", "Fanny videos", "Gess the song"]
for i in titles:
    print(i)
new_title = input("Enter a name of the TV program: ")
titles.append(new_title)
num = int(input("Enter a position: "))
titles.insert(num, new_title)
for i in titles:
    print(i)

