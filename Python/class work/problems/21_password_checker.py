correct_password = "SecurePass123"
chance = 5
while chance > 0:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid password")
        chance -= 1
        print(chance,"more chances")
    if chance == 0:
        print("Maximum attempts reached. Account locked!")