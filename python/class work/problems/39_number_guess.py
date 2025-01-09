# Number Guessing Game
import random

random_num = random.randint(1,100)
guess = 0

while True:
    guess += 1
    print(f"Attempt {guess}: Guess the Number!")
    guess_num = int(input("Enter a Number from 1-100: "))

    if guess_num > random_num:
        print("Too High")
    elif guess_num < random_num:
        print("Too Low")
    else:
        print("Congratulations Correct Number!")
        break

    if guess == 10:
        print()
        print("Max Attempt Reached!")
        print("Correct Number: ", random_num)
        break
    print()