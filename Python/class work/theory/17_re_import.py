import re

# \d ---> digit
# \D ---> Any character except digit
#  . ---> Any character except a new line
# \w-----> Any alphanumeric characters
# \W-----> Any non alphanumeric characters
# \s-----> Any whitespace
# \S-----> Any non whitespace
# + -----> One or more repetitions
# * -----> 0 or more repetitions
# ? -----> 0 or 1 repetition
# []-----> Matches any one of the characters inside the brackets

str1 = "abcdeabcs 1 0a a s 7039020200 $#@^(*(%$@!))"

pattern = re.compile(r"\d")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\d\d\d\d")
print(pattern.findall(str1))
print()
pattern = re.compile(r"\d{4}")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\D")
print(pattern.findall(str1))
print()

pattern = re.compile(r".")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\w")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\W")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\s")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\S")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\d+")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\d *")
print(pattern.findall(str1))
print()

pattern = re.compile(r"\D ?")
print(pattern.findall(str1))
print()

pattern = re.compile(r"[0-9a-zA-Z]")
print(pattern.findall(str1))
print()