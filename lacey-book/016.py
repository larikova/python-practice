question1 = input("Is it raining today? ")
question1 = str.lower(question1)
if question1 == "yes":
    question2 = input("Is it windy today? ")
    question2 = str.lower(question2)
    if question2 == "yes":
        print("It is too windy for an umbrell")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
