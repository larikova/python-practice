f = int(input())
e = f % 10
d = f % 100 // 10
s = f % 1000 // 100
t = f // 1000
p = e * 10 + d
o = f // 100
ans = (o - p) + 1
print(ans)

# e = f % 100
# k = f // 100
# e = d * 10 + c
# k = f // 100
