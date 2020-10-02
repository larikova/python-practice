postcode = input("Enter your postcode: ")
lenght = len(postcode)
postcode = str.upper(postcode[0:2]) + postcode[2: lenght]
print(postcode)
