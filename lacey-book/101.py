sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
         "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
         "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
         "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}

name = input("Enter a name: ")
region = input("Enter a region: ")
print("The salary is", sales[name][region])

name2 = input("Enter a name: ")
region2 = input("Enter a region: ")
newSale = int(input("Enter a new salary: "))
sales[name2][region2] = newSale
print((name2), sales[name2])
