# list comprehension syntax
# [expression for i in iterables if condition]

# basic syntax
lst = [i for i in range(1,101)]
print(lst)

# with condition
lst = [i for i in range(1,101) if i % 2 == 0]
print(lst)

# starting with a
lst = ["abc","bcd","sass","acc","ayyy"]
lst = [i for i in lst if i.startswith("a")]
print(lst)

# length of strings
lst = ["abc","bcd","sass","acc","ayyy"]
lst = [len(i) for i in lst]
print(lst)