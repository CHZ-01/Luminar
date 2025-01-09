# hw03
lst1 = [10, 20, 30, 40] 
lst2 = [100, 200, 300, 400]

for i in range(len(lst1)):
    print(lst1[i],end=" ")
    for j in range(1):
        i += 1
        print(lst2[-i])