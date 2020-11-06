array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Enter a number of row: "))
print(array[row])
value = int(input("Enter a number: "))
array[row].append(value)
print(array[row])
