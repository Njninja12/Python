
import random

again = "yes"

while again == "yes":

    magic_num = random.randint(1, 100)

    guess_count = 0
    guess = -1

    while guess != magic_num:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1

        if guess > magic_num:
            print("Lower")
        elif guess < magic_num:
            print("Higher")
        else:
            print("You guessed it!")

    print(f"It took you {guess_count} tries to guess the number.\n")

    again = input("Would you like to play again? ").lower()

print("Thanks for playing!")

