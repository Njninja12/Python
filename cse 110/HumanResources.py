with open("hr_system.txt") as Human_Resources:
    for line in Human_Resources:
        parts = line.split()
        name = parts[0]
        id_num = parts[1]
        title = parts[2]
        salary = float(parts[3])

        paycheck = salary/24
        if title == "Engineer":
            paycheck += 1000

        # print(f"Name: {name}, Title: {title}")
        print(f"{name} (ID: {id_num}), {title} - ${paycheck:.2f}")