poem = "A hundred bad days made a hundred good stories"
print(poem)
print()
print("Enter 2 numbers between 0 and", len(poem))
print()
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))
print(poem[start: end])
