a={1,2,3}
b={1,2,3,4,5}

var = a.union(b)
print(var)
var = b.union(a)
print(var)

var = a.intersection(b)
print(var)
var = b.intersection(a)
print(var)

var = a.difference(b)
print(var)
var = b.difference(a)
print(var)

var = a.isdisjoint(b)
print(var)

var = a.issubset(b)
print(var)

var = a.issuperset(b)
print(var)
var = b.issuperset(a)
print(var)

lst1 = [1,2,3,5,7]
lst2 = [2,4,5,7,8,9]
lst3 = list(set(lst1).intersection(set(lst2)))
print(lst3)

lst1 = [123,42,4,2,323,3]
lst2 = [12,34,235,5,21]
if set(lst1).isdisjoint(set(lst2)):
    print("No common elements found")
else:
    print("common elements found")

day1 = {1,2,3,4,5}
day2 = {2,3,4,5,6}
day3 = {3,4,5,6,7}
check = day1.intersection(day2.intersection(day3))
print(check)
