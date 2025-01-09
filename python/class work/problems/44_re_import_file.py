import re

with open(r"class work\problems\file\regular_expression.txt","r") as obj:
    data = obj.read()

emails = re.compile(r"[a-zA-Z0-9]+@gmail.com")
print(emails.findall(data))

phones = re.compile(r"\d{3}-\d{3}-\d{4}")
print(phones.findall(data))

pins = re.compile(r"[A-z]{2} (\d{5})")
print(pins.findall(data))

names = re.compile(r"([a-zA-Z]+[a-zA-Z]+)\n\d{3}-\d{3}-\d{4}")
print(names.findall(data))

