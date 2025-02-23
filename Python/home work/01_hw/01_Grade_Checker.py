mark=int(input("Enter your mark: "))

if mark <=100 and mark >= 90:
    print("A grade")
elif mark <= 89 and mark >= 80:
    print("B grade")
elif mark <= 79 and mark >= 70:
    print("C grade")
elif mark <= 69 and mark >= 60:
    print("D grade")
elif mark <= 59 and mark >= 0:
    print("F grade")
else:
    print("Invalid mark")
    