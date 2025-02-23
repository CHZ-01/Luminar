import random

var = random.randint(1,100)
print(var)

lst = ["a", "b", "c", "d", "e"]
random_item = random.choice(lst)
print(random_item)

print(lst)
random.shuffle(lst)
print(lst)

var = random.random()
print(var)