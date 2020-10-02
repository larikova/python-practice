a = int(input())
b = int(input())
toggle = 1
a1 = toggle * (a // b) * a
toggle -= (a // b)
b1 = toggle * (b // a) * b
c = a1 + b1
print(c)
