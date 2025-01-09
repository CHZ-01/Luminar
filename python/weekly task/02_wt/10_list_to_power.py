# hw10 list to square & cube
lst = input("Enter the list numbers separated by Spaces: ").split()
new_lst = []
final_lst = []

for i in lst:
    new_lst.append(int(i))

print("Your List: ",new_lst)

for i in new_lst:
    if i % 2 == 0:
        final_lst.append(i**2)
    else:
        final_lst.append(i**3)

print("Final List: ", final_lst)