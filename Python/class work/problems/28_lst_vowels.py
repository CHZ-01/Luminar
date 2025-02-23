lst = ["banana", "apple", "orange", "grapes"]
vowels = "aeiouAEIOU"

for i in lst:
    c = 0
    for j in i:
        if j in vowels:
            c += 1
    print(f"vowels in {i}: {c}")