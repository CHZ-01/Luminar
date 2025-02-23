unit=int(input("Enter your electricity usage(in units): "))

if 0 <= unit <= 100:
    cost = unit * 3
elif 100 < unit <= 200:
    unit -= 100
    cost = 100 * 3 + unit * 4.5
elif 200 < unit <= 300:
    unit -= 200
    cost = 100 * 3 + 100 * 4.5 + unit * 6
elif unit > 300:
    cost = unit * 7
else:
    print("Invalid unit entry")

print("Your Electricity bill is: Rs.", cost , sep="")