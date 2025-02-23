# *args is a function to take multiple arguments
def add(datatype, *args):

    # if datatype is int initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str initialize answer as ''
    if datatype == 'str':
        answer = ''

    # calling each arguments separately
    for x in args:
        # this will do addition or concatenation according to the datatype
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Python')



def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum(5,6))
