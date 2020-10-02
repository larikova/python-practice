import random

num = random.randint(1, 5)
guess = int(input("Enter a number between 1 and 5 "))
if num == guess:
    print("Well done")
elif num > guess:
    print("Too low")
else:
    print("Too high")
guess2 = int(input("Enter a second number between 1 and 5 "))
if num == guess2:
    print("Correct")
else:
    print("You lose")
print(num)
