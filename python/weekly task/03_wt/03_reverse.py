# hw03 Reverse input string
word = input("Enter a word: ")
length = len(word)
i = length - 1

# print("Reversed word: ",end="")
# while i >= 0:
#     print(word[i], end="")
#     i -= 1

new = ""
for i in word:
    new = i + new
print("Reversed word: ", new)