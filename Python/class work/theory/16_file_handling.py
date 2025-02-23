# file handling

# read mode
# only supports reading
with open(r"class work\theory\file\test.txt", "r") as obj:
    content = obj.read()
    print(content)

# write mode
# to edit text content
# it clears the existing content and returns the new content
# cannot read
with open(r"class work\theory\file\text1.txt", "w") as obj:
    obj.write("This is a new line\n")
    for i in range(1, 1001):
        obj.write(f"{i}\n")

# append mode
# doesn't clear the existing content
# adds the new content at the end of the existing content
with open(r"class work\theory\file\text2.txt", "a") as obj:
    obj.write("This is an additional line\n")

# r+ mode
# performs read + write operations
# prioritize reading
# cursor point at start by default
with open(r"class work\theory\file\test.txt", "r+") as obj:
    obj.write("This is an additional line\n")
    print(obj.read())

# w+ mode
# performs write + read operations
# prioritize writing
# clears the existing content then performs read or write operations
with open(r"class work\theory\file\text1.txt", "w+") as obj:
    obj.write("This is an additional line\n")
    print(obj.read())

# a+ mode
# performs append + read operations
# prioritize appending
# cursor point at end by default
with open(r"class work\theory\file\text2.txt", "a+") as obj:
    obj.write("This is an additional line\n")
    print(obj.read())