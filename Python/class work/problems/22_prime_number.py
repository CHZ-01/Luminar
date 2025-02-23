num = int(input("Enter a number: "))
count = 0
lst = []

# using for loop
for i in range(1,num+1):
    if num % i == 0:
        count += 1 
        lst.append(i)
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
print("Divisible Numbers:",lst)

# using while loop
# i = num
# while i > 0:
#     if num % i == 0:
#         count += 1
#     i -= 1    
# if count == 2:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

