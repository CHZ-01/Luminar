# hw10
words = ["apple","banana","cherry","date","elderberry"]
skip = ["banana","date"]

for i in words:
    if i in skip:
        continue
    print(i, end=" ")