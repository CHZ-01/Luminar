# def function_name(parameters):
#     body of code
# function_name(parameter's value)


# qn01
def greetings(name="py"):
    print("Welcome", name)
    
greetings("Vaisakh")
greetings()

# qn02
def division(a=1,b=1):
    print("Division: ", a/b)

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
division(a,b)
division(10,2)
division()

# qn03
def odd_even(num):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

num = int(input("Enter a number: "))
odd_even(num)

# qn04
def largest(a,b,c):
    print("Largest: ",max(a,b,c))

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))
largest(a,b,c)

# qn05
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial: ",factorial(num))

# qn06
def average(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

lst = [98, 72, 23, 84, 95]
print("Average: ", average(lst))

# qn07
def reverse(word):
    return word[::-1]

word = input("Enter a word: ")
print("Reversed word: ", reverse(word))

# qn08
def palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
if palindrome(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome")

# qn09
def counter(word):
    vowel = "aeiouAEIOU"
    count = 0
    for i in word:
        if i in vowel:
            count += 1
    return count

word = input("Enter a word: ")
print("Number of vowels: ", counter(word))

# qn10
def intersect(lst1,lst2):
    return list(set(lst1).intersection(set(lst2)))

lst1 = [1,2,3,4,5]
lst2 = [3,4,5,6,7]
print("Intersection: ", intersect(lst1, lst2))

# qn11
def prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

num = int(input("Enter a number: "))
print(f"prime check, {prime(num)}")

# qn12
def anagram(word1,word2):
    return sorted(word1) == sorted(word2)

word1 = input("Enter the First word: ")
word2 = input("Enter the Second word: ")
if anagram(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")

# qn13
def longest(sen):
    words = sen.split()
    long = ""
    for i in words:
        if len(i) > len(long):
            long = i
    return long

sen = input("Enter the sentence: ")
print("Longest word:", longest(sen))

# qn14
def counter(sen):
    dict1 = {}
    for i in sen:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

sen = input("Enter a sentence: ")
print("Character count:", counter(sen))

# qn15
def gcd(num1,num2):
    cd = 0
    for i in range(1,num1+1):
        if num1 % i == 0 and num2 % i == 0:
            cd = i
    return cd

num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))

# qn16
def prime(mini, maxi):
    count = 0
    prime_lst = []
    for i in range(mini, maxi+1):
        count = 0
        for j in range(mini, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            prime_lst.append(i)
    return prime_lst

mini = int(input("Enter min number: "))
maxi = int(input("Enter max number: "))
print("Prime numbers between", mini, "and", maxi, "are:", prime(mini, maxi))                

# qn17
def armstrong(num):
    length = len(str(num))
    sum = 0
    for i in str(num):
        sum += int(i) ** length
    return sum == num

num = int(input("Enter a number: "))  
if armstrong(num):
    print("Armstrong number")
else:
    print("Not Armstrong number")

# qn18
def words(word1,word2):
    lst1 = word1.lower().split()
    lst2 = word2.lower().split()
    return list(set(lst1).intersection(lst2))

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print("common strings: ",words(word1,word2))

# qn19
def fibonacci(num):
    a = 0
    b = 1
    for i in range(0,num+1):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

num = int(input("Enter the number: "))
fibonacci(num)