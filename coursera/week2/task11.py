# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 > 0 and x2 > 0:
#     if y1 > 0 and y2 > 0:
#         print("YES")
#     else:
#         if y1 < 0 and y2 < 0:
#             print("YES")
#         else:
#             print("NO")
# else:
#     if x1 < 0 and x2 < 0:
#         if y1 < 0 and y2 < 0:
#             print("YES")
#         else:
#             if y1 > 0 and y2 > 0:
#                 print("YES")
#             else:
#                 print("NO")
#     else:
#         print("NO")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0:
    x1 = 1
if x1 < 0:
    x1 = -1
if x2 > 0:
    x2 = 1
if x2 < 0:
    x2 = -1
if y1 > 0:
    y1 = 1
if y1 < 0:
    y1 = -1
if y2 > 0:
    y2 = 1
if y2 < 0:
    y2 = -1
if x1 == x2 and y1 == y2:
    print("YES")
else:
    print("NO")
