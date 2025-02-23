var1 = input("Enter a number: ")
lst = []

for i in var1:
    lst.append(i)

if lst == lst[::-1]:
    print("The given number is a palindrome.")
else:
    print("The given number is not a palindrome.")