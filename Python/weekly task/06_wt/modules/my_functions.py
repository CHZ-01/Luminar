# hw03
def count(word):
    vowels = "aeiouAEIOU"
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count

def reverse(word):
    return word[::-1]