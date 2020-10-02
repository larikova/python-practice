print("1) Square")
print("2) Triangle")
num = int(input("Enter a number: "))
if num == 1:
    length = int(input("Enter length of one of the sides: "))
    areaSquare = length ** 2
    print(areaSquare)
elif num == 2:
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    areaTriangle = (base * height) / 2
    print(areaTriangle)
else:
    print("Error")
