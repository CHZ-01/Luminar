# while condition(true or false):
#   block of code
#   increment or decrement

# example
i = 1
while i <= 5:
    print(i)
    i += 1

# sum
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print(sum)

# even sum
i = 200
sum = 0
while i <= 1000:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

# first 20 even sum
i = 20
count = 1
even = 0
while i > 0:
    if count % 2 == 0:
        even += count
        i -= 1
    count += 1
print(even)

# sum of first 10 multiples of 3 and 7
i = 10
count = 1
multiple = 0

# print(multiple)
while i > 0:
    if count % 3 == 0 and count % 7 == 0:
        multiple += count
        i -= 1
    count += 1


# factorial
i = int(input("Enter a number: "))
fact = 1

while i > 0:
    fact *= i
    i -= 1

print(f"Factorial: {fact}")