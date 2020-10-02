a = int(input())
b = int(input())
f = (a % b + b - 1) // b
print('YES' * (1 - f), 'NO' * f, sep='')
