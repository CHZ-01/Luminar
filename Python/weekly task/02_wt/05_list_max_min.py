# hw05 min max
lst = input("Enter the list elements separated by Spaces: ").split()
new_lst = []

for i in lst:
    new_lst.append(int(i))

print("Your list is: ",new_lst)    

maxi = max(lst)
print("Maximum number in the list: ",maxi)

mini = min(lst)
print("Minimum number in the list: ",mini)