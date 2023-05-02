
print("Please enter the following information:")
print()

first = input("First Name: ")
last = input("Last Name: ")
email = input("Email Address: ")
phone = input("Phone Number: ")
job = input("Job Title: ")
idnum = input("ID Number: ")
hair = input("Hair color: ")
eye = input("Eye color: ")
month = input("Month started: ")
train = input("Completed additional training? ")

# placed a \n command to make a blank line
print("\nThe ID Card Is: ")
print("----------------------------")
print(f"{last.upper()}, {first.capitalize()}")
print(job.title())
print(f"ID: {idnum}")
print()
print(email.lower())
print(phone)
# Stretch portion of the activity
print()
print()
print(f"Hair: {hair:15} Eyes: {eye}")
print(f"Month: {month:14} Training: {train}")

print("----------------------------")