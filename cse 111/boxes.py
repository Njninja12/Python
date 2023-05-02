import math

# User input for the amount of items per box and how many items in total.

item_amount = int(input("Enter the number of items: "))
per_box = int(input("Enter the number of items per box: "))


boxes = math.ceil(item_amount / per_box)


print(f"For {item_amount} items, you need {boxes} boxes.")