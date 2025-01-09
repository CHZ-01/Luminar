# hw10
string = input("Enter a String: ")
check = ""

for i in string:
    if i not in check:
        check += i
    else:
        check += " "

lst = check.split()
print("Longest substring without repeating characters:", max(lst))