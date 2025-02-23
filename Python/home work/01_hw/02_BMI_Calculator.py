weight=float(input("Enter your weight(kg): "))
height=float(input("Enter your height(m): "))
bmi=weight/(height**2)
print("Your BMI is: ", bmi, "and you are", end=" ")

if bmi >= 30:
    print("Obese")
elif bmi <= 29.9 and bmi >= 25:
    print("Overweight")
elif bmi <= 24.9 and bmi >= 18.5:
    print("Normal weight")
elif bmi < 18.5:
    print("Underweight")
