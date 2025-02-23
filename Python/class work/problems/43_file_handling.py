# palindrome
with open(r"class work\problems\file\text.txt","r") as obj:
    content = obj.read().split()
    for i in content:
        if i == i[::-1]:
            print(i)


# words with W
import string

with open(r"class work\problems\file\sample_text.txt","r") as obj:
    data = obj.read()

lst = [i.strip(string.punctuation+" ") for i in data.split()]

with open(r"class work\problems\file\text1.txt","w") as obj:
    for i in lst:
        if i.startswith("w") or i.startswith("W"):
            obj.write(f"{i}\n")


# user input to new file
with open(r"class work\problems\file\text3.txt", "w") as obj:
    while True:
        user_input = input("Input: ")
        if user_input.lower() == "exit":
            break
        else:
            obj.write(user_input + "\n")


# replace words
with open(r"class work\problems\file\sample_text.txt", "r") as obj:
    data = obj.read().lower()
    
with open(r"class work\problems\file\text4.txt", "w+") as obj:
    obj.write(data.replace("license", "permit"))


# python count
with open(r"class work\problems\file\sample_text.txt", "r") as obj:
    data = obj.read().split()
    count = 0
    for i in data:
        if i.lower() == "python":
            count += 1
    print("No of python in file: ", count)


# python extract
with open(r"class work\problems\file\sample_text.txt", "r") as obj:
    data = obj.readlines()

with open(r"class work\problems\file\text5.txt", "w") as obj:
    for i in data:
        if "python" in i.lower():
            obj.write(i)


# data reverse
with open(r"class work\problems\file\sample_text.txt", "r") as obj:
    data = obj.readlines()

with open(r"class work\problems\file\text6.txt", "w") as obj:
    for i in data:
        obj.write(i[::-1])


# longest line 
with open(r"class work\problems\file\sample_text.txt", "r") as obj:
    data = obj.readlines()
    length = 0
    longest = ""
    for i in data:
        if len(i) > length:
            longest = i
            length = len(i)
    print(f"Longest line: {longest}")
    print(f"Length: {length}")


# uppercase
with open(r"class work\problems\file\sample_text.txt", "r") as obj:
    data = obj.read()

with open(r"class work\problems\file\text7.txt", "w") as obj:
    obj.write(data.upper())