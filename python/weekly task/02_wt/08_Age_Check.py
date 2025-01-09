# hw08 Voting Eligibility
age = int(input("Enter your Age: "))

if age >= 18 and age <= 120:
    print("You are eligible for voting")
elif age >=0 and age < 18:
    print("You are not eligible for voting")
else:
    print("Invalid age")