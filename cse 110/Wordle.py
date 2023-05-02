
secret_word = "saint"

hint = " _ " * len(secret_word)

print(f"Your hint is:{hint}")
guess = input("What is your guess? ")
guess_count = 0

while guess.lower() != secret_word.lower():
    print("That is incorrect.")
    guess = input("What is your guess? ")
    guess_count = guess_count + 1

print("That is correct! Congrats!")
print(f"It took you {guess_count} tries.")
print("Thanks for playing.")