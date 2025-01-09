num=int(input("Enter a number: "))

if num > 0:
    print("Positive number")
    if num < 10:
        print("Small number")
    elif 10 <= num < 100:
        print("Medium number") 
    elif num >= 100:
        print("Large number")        
elif num < 0:
    print("Negative number")
elif num == 0:
    print("Zero")        
else:
    print("Invalid input")    