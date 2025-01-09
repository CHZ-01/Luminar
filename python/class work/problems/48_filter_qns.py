# filter(function,iterables)
# prints only when True 

# vowels
char = ["a","v","b","c","e","h","g","u","i","p","o"]
var = list(filter(lambda i : i.lower() not in "aeiou",char))
print(var)

# palindrome
def palindrome(s):
    return s == s[::-1]

string = ["level", "world", "radar", "python", "refer","programming"]
var = list(filter(palindrome,string))
print(var)

# prime
def prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    return count == 2 or num == 1
        
num = [1,10,20,7,219,317,313,13,2,153,1]
var = list(filter(prime,num))
print(var)

# armstrong
def armstrong(num):
    sum = 0
    for i in str(num):
        sum += int(i) ** len(str(num))
    return sum == num
num = [1,10,20,7,219,317,313,13,2,153,1]
var = list(filter(armstrong,num))
print(var)

# negative values
num = [1,11,-120,-912,20,0]
var = list(filter(lambda x: x < 0, num))
print(var)

# 2 digit even
num = [1,312,3,23,44,12,55,234,22]
var = list(filter(lambda i: i > 9 and i < 100 and i % 2 == 0, num))
print(var)

# length of 5
word = ["level","world","radar","python","refer","programming"]
var = list(filter(lambda i: len(i) == 5, word))
print(var)