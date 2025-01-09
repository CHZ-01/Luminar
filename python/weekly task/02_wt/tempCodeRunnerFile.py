word = input("Enter a Word: ")
c=0
for i in word:
    if c%2 == 0:
        word += i
        print("Even index values: ", word[c], end="")
    c+=1