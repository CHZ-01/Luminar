num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=0
for i in range(num1, num2+1):
    if i%2==0:
        print(i, end=' ')
        sum+=i
print()
print(f"Sum of even numbers between {num1} and {num2}: {sum}")
