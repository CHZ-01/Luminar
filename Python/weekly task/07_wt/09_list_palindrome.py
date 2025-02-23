# hw09
inp = input("Enter the list elements: ")
lst = list(map(str,inp.split()))
print("List: ",lst)

if lst == lst[::-1]:
    print("List is a Palindrome")
else:
    print("List is not a Palindrome")