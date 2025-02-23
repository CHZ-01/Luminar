num = int(input("Enter a number: "))
last = num % 10

if last % 3 == 0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")    