sen="the big dwarf only jumps"
lst=[]
set1=set()

for i in sen:
    if i.isalpha():
        lst.append(i)
        set1.add(i)

if len(lst)==len(set1):
    print("heterogram")
else:
    print("not heterogram")
