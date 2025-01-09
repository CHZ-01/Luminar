lst = [[34,1,23,32],[23,12,44,2,3]]

print(lst[1][0])

lst[0][-1] = "new"
print(lst)

lst[1].pop()
print(lst)

lst[0].insert(2,999)
print(lst)

lst[0].extend(lst[1])
print(lst)