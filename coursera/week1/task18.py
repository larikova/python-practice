n = int(input())
sec = (n % 60)
min = (n // 60 % 60)
h = (n // 60 // 60 % 24)
print(h, end='')
print(':', end='')
print(min // 10, min % 10, end='', sep='')
print(':', end='')
print(sec // 10, sec % 10, sep='')

# print(h, end='')
# print(':', end='')
# print(min, end='')
# print(':', end='')
# print(sec)
