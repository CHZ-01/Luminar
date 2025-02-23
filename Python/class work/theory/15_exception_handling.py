# raise Exception it is used for creating an error message.
a=int(input("Enter a number: "))
if a<0:
    raise ValueError
print(a)


# except Exception it is used for all kind of exceptions.
# except(value error,zero division error) it is used for multiple exceptions.
try:
    a=int(input("Enter a first number: "))
    b=int(input("Enter a second number: "))
    print(a/b)
except ZeroDivisionError: # it is used for zero division errors.
    print("Zero Division Not Possible, please enter valid numbers.")
finally: # it is always executes in any circumstances.
    print("Print Anyways")


# try, except, else, finally
lst=[1,23,45,67,89,99]
try:
  for i in range(10):
    print(lst[i])
except IndexError:
    print("Index out of range. List length is", len(lst))
finally:
    print("This code block is always executed.")
    

# try, multiple except, else, finally
lst=[1,23,45,67,89,"99"]
try:
    for i in range(7):
        print(lst[i]+1)
except (IndexError,TypeError):
    print("Index out of range")
finally:
    print("This code block is always executed.")