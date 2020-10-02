n = int(input())
if 11 <= n <= 14:
    print(n, "korov")
else:
    if n % 10 == 1:
        print(n, "korova")
    else:
        if 2 <= n % 10 <= 4:
            print(n, "korovy")
        else:
            print(n, "korov")
