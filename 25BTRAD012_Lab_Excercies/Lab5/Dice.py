import random

while True:
    n = int(input("Enter number of dice to roll: "))

    for i in range(n):
        result = random.randint(1, 6)
        print("Dice", i + 1, ":", result)

    choice = input("Roll again? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for playing!")
        break