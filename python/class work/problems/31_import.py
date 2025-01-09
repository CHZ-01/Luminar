import string
str1 = "python,. @! pro$%gramming"
new = ""

for i in str1:
    if i not in string.punctuation:
        new += i

print(new)