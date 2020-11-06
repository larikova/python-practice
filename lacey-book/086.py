password1 = input("Enter your new password: ")
password2 = input("Enter your password again: ")
if password1 == password2:
    print("Thank you")
elif password1.lower() == password2 or password2.lower() == password1:
    print("They must be in the same case")
else:
    print("Incorrect")
