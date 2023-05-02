
# create an if - elif - else function to determine the grade.

percent = float(input("What percentage did you get? "))
# If else functions will print the letter grade depending on the percentage
if percent >= 90:
    print("Your grade is an A")
elif percent >= 80:
    print("Your grade is a B")
elif percent >= 70:
    print("Your grade is a C")
elif percent >= 60:
    print("Your grade is a D")
else:
    print("Your grade is a F")

# If grade is above a 70 then print a congrats message if not then encourage
# to try again next year.

if percent >= 70:
    print("Congrats!! You passed!")
else:
    print("I'm sorry, you did not pass. Hopefully you'll do better next time.")