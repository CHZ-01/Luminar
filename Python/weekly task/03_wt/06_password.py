# hw06 input correct password
password = "secret"

for i in range(1,4):
    print(f"Attempt {i} of 3")
    user_password = input("Enter your password: ")
    if user_password == password:
        print("Login successful!")
        break
    else:
        print("Invalid Password, Login failed!")    
