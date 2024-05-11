print("Welcome to the Guessing Game!")

name=input("enter your name=")
print(name,"welcome to the no. guessing game")
import random

print("Select difficulty level:")
print("1. Easy (7 attempts)")
print("2. hard (5 attempts)")


difficulty = int(input(f"{name}Enter your choice (1/2): "))
if difficulty == 1:
    max_attempts = 7
elif difficulty == 2:
    max_attempts = 5
else:
    print(f"Invalid choice.{name} Defaulting to easy difficulty.")
    max_attempts = 7

secret_number = random.randint(1, 100)
attempts = 0

print(f"You have {max_attempts} attempts to guess the secret number between 1 and 100.")

while attempts < max_attempts:
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
        break
else:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}. Try again!")