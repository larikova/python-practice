name = input('Enter your name: ')
letter = len(name)
count = 0
name = name.lower()
for i in range(0, letter):
    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u' or name[i] == 'y':
        count = count + 1
print("Your name has", count, "Vowels")
print("Your name has", letter, "letters")
