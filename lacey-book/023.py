rhyme = input("Enter the first line of a nursery rhyme: ")
length = len(rhyme)
print("The length of the nursery rhyme has ", length)
start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
start = start -1
#end = end -1
print(rhyme[start:end])
