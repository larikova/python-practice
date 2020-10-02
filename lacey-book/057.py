import random

score = 0
for i in range(1,6):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = num1 + num2
    print(num1, "+", num2)
    guess = int(input("Enter an answIMG_7275.JPGer: "))
    if guess == answer:
        score = score + 1
print("Your score is", score)



