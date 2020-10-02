word = input("Enter a word ")
word = word.lower()
let = word[0:1]
if let == "a" or let == "e" or let == "i" or let == "o" or let == "y":
    print(word + "way")
else:
    d = len(word)
    wordnew = word[1:d]
    print(wordnew + let + "ay")
