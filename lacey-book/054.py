import random

question = random.choice(["heads", "tails"])
answer = input("Choose 'heads' or 'tails', please: ")
if question == answer:
    print("You win !!!")
else:
    print("Bad luck :(( ")
print("Computer selected", question)
