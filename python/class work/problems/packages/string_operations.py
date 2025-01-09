def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return s.capitalize()

def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for i in s:
        if i.lower() in vowels:
            count += 1
    return count
    # return sum(1 for char in s.lower() if char in vowels)