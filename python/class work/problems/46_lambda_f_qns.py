# uppercase
var = lambda s: s.upper()
print(var(input("Enter a string: ")))

# modulus
var = lambda n1,n2: n1%n2
n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))
print("Modulus: ", var(n1, n2))

# squared sum of three
var = lambda n1,n2,n3: (n1*n1)+(n2*n2)+(n3*n3)
n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))
n3 = int(input("Enter Third number: "))
print("Squared sum: ", var(n1, n2,n3))

# first word
var = lambda s: s[0]
print(var(input("Enter a string: ").split()))
# var = lambda s: s.split()[0]
# print(var(input("Enter a string: ")))

# last word
var = lambda s: s[-1]
print(var(input("Enter a string: ").split()))
# var = lambda s: s.split()[-1]
# print(var(input("Enter a string: ")))