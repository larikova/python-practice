a = int(input())
b = int(input())
c = int(input())
if a == c or a == b or b == c:
    print("2")
else:
    if a == b == c:
        print("3")
    else:
        if a != b and b != c:
            print("0")
