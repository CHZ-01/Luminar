dict1 = {"a": 1, "b": 2, "c": 3, "d": [1,2,3]}
print(dict1)

dict1["d"] = 4
print(dict1)

dict1["e"] = 5
print(dict1)

dict1 = {"a": 1, "b": 2, "c": 3, "d": [1,2,3]}

dict1.pop("b")
# print(dict1.pop("b"))
print(dict1)
# dict1.popitem()
print(dict1.popitem())
print(dict1)

dict1.update({"f": 6, "g": 7, "h": 8})
print(dict1)

keys = [1,2,3,4,5]
values = ["a", "b", "c", "d"]
dict1=dict(zip(keys,values))
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

var1 = [(1,"a"),(2,"b"),(3,"c")]
dict1 = dict(var1)
print(dict1)

names = ["name1", "name2", "name3"]
marks = [90,95,99]
for i in zip(names,marks):
    print(i)
for i,j in zip(names,marks):
    print(i,j)

dict1 = {"a": {1:{2:"hello"},2:{1:"find me"}}, "b": 2, "c": 3}
print(dict1["a"][1][2])
print(dict1["a"][2][1])

sample = {"class": {"student":{"name": "mike", "mark": {"physics": 70,"history":80}}}}
print(sample["class"]["student"]["mark"]["history"])
sample["class"]["student"]["mark"]["maths"] = 90
sample["class"]["student"]["mark"]["physics"] = 60
print(sample)
