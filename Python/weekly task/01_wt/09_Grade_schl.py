# hw09 School Grade
mark=int(input("Enter your mark: "))

if mark <=100 and mark > 80:
    print("A grade")
elif mark <= 80 and mark > 60:
    print("B grade")
elif mark <= 60 and mark > 50:
    print("C grade")
elif mark <= 50 and mark > 45:
    print("D grade")
elif mark <= 45 and mark > 25:
    print("E grade")
elif mark <= 25 and mark > 0:
    print("F grade")
else:
    print("Invalid mark")
    