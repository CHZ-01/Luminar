str = input("Enter a word: ")
str_rev = str[::-1]

if str == str_rev:
    print(str,"is Palindrome")
else:
    print(str,"is not Palindrome")    