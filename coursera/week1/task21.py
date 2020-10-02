h = int(input())
a = int(input())
b = int(input())
c = a - b
l = h - b
wholePart = l // c
fractionalPart = ((l % c) + (c - 1)) // c
result = wholePart + fractionalPart
print(result)
