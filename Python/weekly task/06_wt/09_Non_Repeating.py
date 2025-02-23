# hw09
word = input("Enter a word: ")
dict1 = {}

for i in word:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 0

for i in dict1:
    if dict1[i] == 0:
        print("First Non-Repeating Character:",i)
        break

