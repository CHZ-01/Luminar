# hw10 Factorial
num = int(input("Enter the number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print(f"Factorial of {num}: {fact}")