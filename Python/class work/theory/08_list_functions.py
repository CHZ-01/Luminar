lst = [123,23,12,4,23,4,21,23,8,5]
print(lst)
print("Length: ", len(lst))
print("Maximum: ", max(lst))
print("Minimum: ", min(lst))
print("Sum: ", sum(lst))

lst.sort()
print("Ascending Order: ", lst)
lst[0] # minimum value
lst[-1] # maximum value

lst.sort(reverse=True)
print("Descending Order: ", lst)