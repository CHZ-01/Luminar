# hw08
n = int(input("Enter the number: "))
lst1 = []
lst2 = []

for i in range(1,n+1):
    lst1.append(i)
    lst2.append(i*i)

sq_dict = dict(zip(lst1,lst2))
print(sq_dict)