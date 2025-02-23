# hw05
def fibonacci(num):
    num1 = 0
    num2 = 1
    for i in range(1,num+1):
        print(num1, end=" ")
        num3 = num1 + num2
        num1 = num2
        num2 = num3

num = int(input("Enter the number of Sequence: "))
fibonacci(num)