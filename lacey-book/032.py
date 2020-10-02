import math

radius = int(input("Enter the radius of a cylinder: "))
depth = int(input("Enter the depth of a cylinder: "))
area = math.pi * (radius ** 2)
cylinder = area * depth
print(round(cylinder, 3))
