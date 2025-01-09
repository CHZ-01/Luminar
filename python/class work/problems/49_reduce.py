# reduce(function,iterables)
# reduces the iterable into single value
# takes two arguments

from functools import reduce

lst = [1,2,3,4,5]

# sum
var = reduce(lambda a,b: a+b, lst)
print(var)

# product
var = reduce(lambda a,b: a*b, lst)
print(var)

# sum of squares
var = reduce(lambda a,b: a+b**2, lst, 0)
print(var)
