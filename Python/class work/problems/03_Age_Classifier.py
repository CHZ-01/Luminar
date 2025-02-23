age=int(input("Enter your Age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age <= 64:
    print("Adult")
    if age <= 35:
        print("Young Adult")
    else:
        print("Middle-Aged Adult")    
elif 65 <= age <= 100:
    print("Senior Citizen")
else:
    print("Invalid age")                