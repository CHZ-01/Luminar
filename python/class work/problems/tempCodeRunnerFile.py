s = 5
for i in range(1,6):
    print(" "*s, end="")
    s -= 1
    for j in range(i):
        print("*", end=" ")
    print()

s = 2
for i in range(4,0,-1):
    print(" "*s, end="")
    s += 1
    for j in range(i):
        print("*", end=" ")
    print()