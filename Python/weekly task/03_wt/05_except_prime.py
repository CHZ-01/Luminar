# hw05 print numbers except for prime numbers
num = int(input("Enter a number: "))

print(f"Number except prime numbers until {num}:")
print("1", end=" ")
for i in range(1,num+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count > 2:
        print(i, end=" ")
