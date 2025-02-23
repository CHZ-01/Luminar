# hw01 3 or 5 divisible numbers
print("Numbers divisible with 3 or 5 until 20: ")

for i in range(1,21):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")