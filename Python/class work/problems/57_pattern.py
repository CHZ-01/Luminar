# to find ascii value
cal = ord("A")
print(cal)

print()
# A
# B B
# C C C
# D D D D
# E E E E E

a = 65
for i in range(5):
    for j in range(i + 1):
        print(chr(a), end=" ")
    a += 1
    print()

