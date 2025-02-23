# hw07 Greatest Number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# greatest = max(num1, num2, num3)
# print(greatest,"is the Greatest number")

if num1 > num2 and num1 > num3:
    print(num1, "is the Greatest")
elif num2 > num1 and num2 > num3:
    print(num2, "is the Greatest")
else:
    print(num3, "is the Greatest")        