# hw04 possible identifiers
import itertools
n = int(input("Enter the length of identifier: "))

lst1 = []
for i in range(n):
    i = input("Enter identifier: ") 
    lst1.append(i)

new_lst = list(itertools.permutations(lst1))

lst2 = []
for i in new_lst:
    lst2.append(''.join(i))
print("All Possible Combinations: ",lst2)

identifier = []
for i in lst2:
    if i.isidentifier():
        identifier.append(i)
print("All Possible Identifiers: ",identifier)