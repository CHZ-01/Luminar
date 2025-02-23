lst = [23,23,5,2,34,20]

for i in lst:
    if i < 0:
        print("Negative numbers found in the list.")
        break
else:
    print("No negative numbers found in the list.")