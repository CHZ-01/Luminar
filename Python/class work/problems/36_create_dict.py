# qn1
string = "hello hi python hi hello the that this this hi"
lst1 = string.split()

# lst2 = []
# for i in lst1:
#     lst2.append(string.count(i))
# dict1 = dict(zip(lst1, lst2))
# print(dict1)

dict2 = {}
for i in lst1:
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i] += 1
print(dict2)

# qn2
dict3 = {}
for i in range(1,11):
    dict3[i] = i*i
print(dict3)

# qn3
for i in dict3:
    if dict3[i] % 2 == 0:
        dict3[i] += 10
print(dict3)

# qn4
lst3 = [5,8,9]
for i in lst3:
    dict3.pop(i)
print(dict3)

# qn5
lst4 = []
for i in dict3:
    if i % 2 == 0:
        lst4.append(dict3[i])
print(lst4)

# qn6
dict4 = {}
for i in lst4:
    if i > 25:
        dict4[i] = "large"
    else:
        dict4[i] = "small"
print(dict4)

# qn7
string = "a32 iSFd f20 kl48"
dict5 = {"alphabets":0,"numbers":0}
for i in string:
    if i.isalpha():
        dict5["alphabets"] += 1
    elif i.isnumeric():
        dict5["numbers"] += 1
print(dict5)