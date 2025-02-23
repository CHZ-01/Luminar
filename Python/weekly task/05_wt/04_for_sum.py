# hw04
lst = [1,10,-45,2,67,-9,56]
sum = 0
for i in lst:
    if i < 0:
        continue
    sum += i
print("Sum:",sum)