msg = input("Enter your msg in uppercase: ")
again = "yes"
while again == "yes":
    if msg.isupper():
        print("Thank you")
        again = "no"
    else:
        print("Try again")
        msg = input("Enter your msg in uppercase: ")
        again = "yes"
