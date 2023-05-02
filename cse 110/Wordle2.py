
secret_word = "shake"


run = "yes"
output = "_ " * len(secret_word)

while run == "yes":

    guess_count = 1
    
    print(f"Your hint is: {output}")
    print()

    print()
    guess = input("What is your guess? ").lower()

    if len(guess) == len(secret_word):


        while guess != secret_word:
            output = ""
            for i in range(len(guess)):
                if guess[i] == secret_word[i]:
                    output += guess[i].upper() + " "
                elif guess[i] in secret_word:
                    output += guess[i].lower() + " "
                else:
                    output += "_ "
                
            print(output)
            guess = input("What is your guess? ")
            guess_count = guess_count + 1

        print("Correct!!!!")
        print("\nThanks for playing!!")
        print(f"It took you {guess_count} tries.")
        run = input("\nWould you like to play again (yes/no)? ")
        output = "_ " * len(secret_word)

    else:
        print("That isn't the correct length. Try again.\n")

print("\nGoodbye")