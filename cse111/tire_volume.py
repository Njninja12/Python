from datetime import datetime
import math

with open("tire_check.txt", "at") as tire_check_file:

    current_date_and_time = datetime.now()
    w = float(input("Enter the width of the tire in mm (ex 205): "))
    a = float(input("Enter the aspect ratio of the tire: (ex 60): "))
    d = float(input("Enter the diameter of the wheel in inches (ex 14): "))
    phone_num = "N/A"
    volume = ((math.pi * w**2) * a * (w*a + 2540*d))/10000000000

    print(f"\n The aproximate volume is {volume:.2f} liters")
    buy = input("\nDo you want to buy tires in these measurements? ").lower()

    if buy == "yes":
        phone_num = input("Enter your phone number: ")
    

    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}, {phone_num}", end="\n", file=tire_check_file)
