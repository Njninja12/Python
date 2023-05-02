
phrase = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

word = "commitment"
fav_letter = input("What is your favorite letter? ")

for letter in word.lower():
    if letter == fav_letter:
        letter = "_"
    print(letter, end="")
          
    
    
    
    
    
    
run = "yes"

while run == "yes":
    user_number = int(input("Please enter a number: "))

    for i, letter in enumerate(phrase):
        # Remember that the % operator divides by a number and returns the remainder.
        # So we can get every 3rd letter by dividing by 3 and looking for a remainder of 0,
        # or more generically, we can divide by the user's number
        if i % user_number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    
    # This puts a newline at the end of the list of quote
    print()

    run = input("Would you like to enter another number? ")

print("Thanks for playing!")
