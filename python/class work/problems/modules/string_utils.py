def reverse_string(word):
    return word[::-1]

def count_vowels(word):
    count = 0
    vowels = "aeiouAEIOU"
    for i in word:
        if i in vowels: 
            count += 1
    return count

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def remove_whitespace(word):
    return word.strip()