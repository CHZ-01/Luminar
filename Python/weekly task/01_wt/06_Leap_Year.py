# hw06 Leap Year
year = int(input("Enter the Year: "))

if ((year % 100) == 0 and (year % 400) == 0) or ((year % 100) != 0 and (year % 4) == 0):
    print(year," is a leap year")
else:
    print(year," is not a leap year")    