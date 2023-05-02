with open("Routes.txt") as dentists:
    for line in dentists:
        parts = line.split(",")
        office_name = parts[0]
        address = parts[1]
        spokesperson = parts[2]
        date_bought = parts[3]
        date_visited = [4]
        