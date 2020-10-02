import random

colour = random.choice(["red", "White", "black", "green", "blue"])
print("red, white, black, green, blue")
tryagain = True
while tryagain == True:
    theirchoice = input("Pick the color: ")
    theirchoice = theirchoice.lower()
    if colour == theirchoice:
        print("Well done")
        tryagain = False
    else:
        if colour == "red":
            print("You are probably feeling RED right now”")
        if colour == "white":
            print("You are probably feeling WHITE right now")
        if colour == "black":
            print("You are probably feeling BLACK right now")
        if colour == "green":
            print("You are probably feeling GREEN right now")
        if colour == "blue":
            print("You are probably feeling BLUE right now")
