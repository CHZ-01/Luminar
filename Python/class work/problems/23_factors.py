num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

lst = []

# using for loop
for i in range(1,num1+1):
    if num1 % i == 0 and num2 % i == 0:
        lst.append(i)
print("Divisible Numbers:",lst)
