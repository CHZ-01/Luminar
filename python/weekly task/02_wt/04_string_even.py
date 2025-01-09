word = input("Enter a Word: ")
c=0

# using for loop
print("Even index values: ", end="")
for i in word:
    if c%2 == 0:
        print(word[c+1], end="")
    c+=1

# using while loop
# c=1
# print("Even index values: ", end="")
# while c<=len(word):
#     if c%2 == 0:
#         print(word[c-1], end="")
#     c+=1