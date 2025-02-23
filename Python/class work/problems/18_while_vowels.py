sen = "python programming languages"
vowels = "aeiouAEIOU"
i = 0
c = 0
print("Sentence:", sen)
print("Vowels in sentence: ", end="")
while i < len(sen):
    if sen[i] in vowels:
        print(sen[i], end="")
        c += 1
    i += 1
print("\nVowels Count:", c)
