# uppercase
lst = ["hello", "world", "python", "programming"]
var = list(map(lambda i: i.upper(), lst))
print(var)

# number & squares
lst = [1,2,3,4]
var = list(map(lambda i: (i,i*i), lst))
print(var)

# vowels
def count(lst):
    vowels = "aeiou"
    count = 0
    for i in lst: 
        if i.lower() in vowels: 
            count+=1
    return count

lst = ["hello", "world", "python", "programming"]
var = list(map(count,lst))
print(var)

# reverse
lst = ["hello", "world", "python", "programming"]
var = list(map(lambda a: a[-1]+a[1:-1]+a[0],lst))
print(var)
