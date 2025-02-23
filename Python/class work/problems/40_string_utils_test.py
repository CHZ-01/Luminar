from modules import string_utils

words = input("Enter the Strings: ")

print("String Reverse:", string_utils.reverse_string(words))

print("String Palindrome:", string_utils.is_palindrome(words))

print("String Vowels Count:", string_utils.count_vowels(words))

print("String Remove WhiteSpaces:", string_utils.remove_whitespace(words))
