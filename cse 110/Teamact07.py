
import random

magic_num = random.randint(1, 100)


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

print("Thanks for playing!")

