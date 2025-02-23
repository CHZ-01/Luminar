str1 = input("Enter first string: ").lower()
str2 = input("Enter first string: ").lower()

sort1 = sorted(str1)
sort2 = sorted(str2)

if sort1 == sort2:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")