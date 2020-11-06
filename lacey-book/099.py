array = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Which row you want to display: "))
print(array[row])
column = int(input("Which column in than row you want to display: "))
print(array[row][column])
ask = input("Do you want to change the value? ")
if ask == "yes":
    newValue = int(input("Enter a number: "))
    array[row][column]= newValue
print(array[row])
