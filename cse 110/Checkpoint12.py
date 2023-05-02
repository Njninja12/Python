
youngest = 1000
youngest_name = ""


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for line in people:
    parts = line.split()
    name = parts[0]
    age = int(parts[1])

    if age < largest:
        largest = age
        new_name = name

print(f"The youngest person is {name}: {age}")
