num = int(input("Enter a number: "))
n1 = 0
n2 = 1
for i in range(num):
    print(n1, end=" ")
    n3 = n1 + n2
    n1 = n2
    n2 = n3
