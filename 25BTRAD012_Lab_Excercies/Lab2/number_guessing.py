import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number guessing game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess :"))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulation! You guess the correct number")
        print("Number of attempts :", attempts)
        break