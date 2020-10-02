a = int(input())
b = int(input())
if a == 1:
    print('YES')
else:
    c = (b - a) + 1
    if (a - 1) % c == 0:
        print("YES")
    else:
        print("NO")

#     if a > 5:
#         print('>5')
#         if a > 8:
#             print('>8')
# else:
#     print('<0')
#     if a < -5:
#         print("<-5")
#         if a < -8:
#             print("<-8")
