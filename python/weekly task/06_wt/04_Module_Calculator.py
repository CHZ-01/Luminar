# hw04
from modules import calculator

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("Addition:", calculator.add(a, b))

print("Subtraction:", calculator.sub(a, b))

print("Multiplication:", calculator.mul(a, b))

print("Division:", calculator.div(a, b))