from packages import string_operations, text_analysis, file_operations

word = input("Enter a String: ")

# Reverse String
reversed_str = string_operations.reverse_string(word)
print("Reversed String: ", reversed_str)

# Capitalize String
capitalized_str = string_operations.capitalize_words(word)
print("Capitalized String: ", capitalized_str)

# Count Vowels
vowel_count = string_operations.count_vowels(word)
print("Vowel Count: ", vowel_count)

# Frequency
Frequency = text_analysis.word_frequency(word)
print("Word Frequency: ", Frequency)

# Unique String
unique_str = text_analysis.unique_words(word)
print("Unique String: ", unique_str)

# Longest String
longest_str = text_analysis.longest_word(word)
print("Longest String: ", longest_str)