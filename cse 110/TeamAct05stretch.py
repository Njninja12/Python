
# create an if - elif - else function to determine the grade.

percent = int(input("What percentage did you get? "))
# If else functions will print the letter grade depending on the percentage
if percent >= 90:
    letter = "A"
elif percent >= 80:
    letter = "B"
elif percent >= 70:
    letter = "C"
elif percent >= 60:
    letter = "D"
elif percent < 60:
    letter = "F"
    
# If grade is above a 70 then print a congrats message if not then encourage
# to try again next year.


# Stretch challenge 1
sign = ""
last_digit = percent % 10

if last_digit >= 7:
    sign = "+"
elif last_digit <= 3:
    sign = "-"
else:
    sign = ""

# Stretch challenge 2

if percent >= 93:
    sign = ""

# Stretch Challenge 3

if letter == "F":
    sign = ""

print(f"Your grade is {letter}{sign}")

if percent >= 70:
    print("Congrats!! You passed!")
else:
    print("I'm sorry, you did not pass. Hopefully you'll do better next time.")
    