data = input("Enter a data: ")

if data.isnumeric():
    data = int(data)
    print("Data entered is Numeric")
else:
    print("Data entered is not Numeric")