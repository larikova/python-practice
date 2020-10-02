import random

num = random.randint(1, 10)
correct = False
while correct == False:
    guess = int(input("Guess the number: "))
    if guess == num:
        correct = True
    elif guess < num:
        print("Too low")
    else:
        print("Too high")
print(num)
