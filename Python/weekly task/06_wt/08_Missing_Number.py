# hw08
set1 = {1,2,3,4,5,6,7,9,10}
set2 = set()

for i in range(1,11):
    set2.add(i)

missing = set2.difference(set1)

print(set1)
print("Missing Number:", missing)