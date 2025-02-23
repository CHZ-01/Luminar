lst = input("Enter the list element separated by spaces: ").split()
print(lst)
new_list = []
for i in lst:
    new_list.append(int(i))
print(new_list)    