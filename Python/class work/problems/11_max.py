list1=[5,1,24,5,52,21]
# print(max(list1))
largest = list1[0]
for i in list1:
    if i > largest:
        largest = i
print("Largest no: ",largest)