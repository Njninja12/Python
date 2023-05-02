
# Week 03 assignment
child_meal = float(input("What is the price of a child meal? "))
adult_meal = float(input("What is the price of an adult meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax = float(input("What is the sales tax rate? "))


child_total = child_meal * children
adult_total = adult_meal * adults
subtotal = adult_total + child_total
print()
print(f"Subtotal: ${subtotal:.2f}")

# Week 04 assignment
sales_tax = tax * subtotal / 100
print(f"Sales Tax: ${sales_tax:.2f}")
# Added a gratuity input asking how much they want to tip.
tip = float(input("Gratuity: "))

total = subtotal + sales_tax + tip
print(f"Total: ${total:.2f}")

print()
payment = float(input("What is the payment amount? "))
amount = payment - total
print(f"Change: ${amount:.2f}")