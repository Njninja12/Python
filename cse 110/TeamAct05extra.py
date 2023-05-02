
# create an if - elif - else function to determine the grade.

percent = float(input("What percentage did you get? "))
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
    
print(f"Your grade is {letter}")
# If grade is above a 70 then print a congrats message if not then encourage
# to try again next year.

if percent >= 70:
    print("Congrats!! You passed!")
else:
    print("I'm sorry, you did not pass. Hopefully you'll do better next time.")