# 1. even from 100 to 150
lst = [i for i in range(100,151) if i % 2 == 0]
print(lst)

# 2. square of each numbers
num = [3,5,8,12,25]
lst = [i*i for i in num]
print(lst)

# 3. odd from 1 to 30
lst = [i for i in range(1,31) if i % 2 != 0]
print(lst)

# 4. first letter
sen = "Python is awesome and versatile"
lst = [i[0] for i in sen.split()]
print(lst)

# 5. remove vowels
sen = "Hello, how are you?"
vowels = "aeiouAEIOU"
lst = "".join([i for i in sen if i not in vowels])
print(lst)

# 6. list of tuples with squares
lst = [(i,i*i) for i in range(1,51) if i % 2 != 0]
print(lst)

# 7. list of tuples with its length
sen = "Python is awesome and versatile"
lst = [(i,len(i)) for i in sen.split()]
print(lst)

# 8. strings to uppercase
low = ["apple","banana","cherry"]
up = [i.upper() for i in  low]
print(up)

# 9. length of list
lst1 = ["data","science","machine","learning"]
lst2 = [(i,len(i)) for i in lst1]
print(lst2)

# 10. with substring ap
lst1 = ["apple","grape","pineapple","fig"]
lst2 = [i for i in lst1 if "ap" in i]
print(lst2) 

# 11. remove spaces
lst1 = ["   trim   ","  spaces  "," here "]
lst2 = [i.strip() for i in lst1]
print(lst2)

# 12. first character
lst1 = ["hello","world","python"]
lst2 = [i[0] for i in lst1]
print(lst2)

# 13. reverse strings
lst1 = ["abc","def","ghi"]
lst2 = [i[::-1] for i in lst1]
print(lst2)

# 14. join hyphen
lst1 = ["a","b","c"]
lst2 = [f"-{i}" for i in lst1]
print(lst2)

# 15. strings shorter than 5
lst1 = ["cat", "elephant", "dog", "giraffe"]
lst2 = [i for i in lst1 if len(i) > 5]
print(lst2)

# 16. capitalize strings
lst1 = ["python","java","c++"]
lst2 = [i.capitalize() for i in lst1]
print(lst2)

# 17. index 2 of strings
lst1 = ["example","test","data"]
lst2 = [i[2:] for i in lst1]
print(lst2)