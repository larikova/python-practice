x1 = int(input())
x2 = int(input())
x3 = int(input())
if x2 <= x1 >= x3:
    a = x1
    b = x2
    c = x3
if x1 <= x2 >= x3:
    a = x2
    b = x1
    c = x3
if x1 <= x3 >= x2:
    a = x3
    b = x2
    c = x1

if a >= b + c or a <= 0 or b <= 0 or c <= 0:
    print("impossible")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("rectangular")
    else:
        if a ** 2 < b ** 2 + c ** 2:
            print("acute")
        else:
            if a ** 2 > b ** 2 + c ** 2:
                print("obtuse")
            else:
                print("impossible")
