n = int(input())  # km per day
m = int(input())  # required km

# days = m // n
# print((days * 24 + 23) // 24)


# speed = (n // 24)
# d = (m // speed)
# print((d + 23) // 24)

# n = 700
# m = 750

print(m // n + (m % n + (n - 1)) // n)

# days = m // n
# print((days * 24 + 23) // 24)
