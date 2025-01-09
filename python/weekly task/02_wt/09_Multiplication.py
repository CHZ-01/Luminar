# hw09 Multiplication Table
num = int(input("Enter the Number to be multiplied: "))

print("Multiplication Table")

for i in range(1,11):
    print(f"{i} X {num} = {i * num}")