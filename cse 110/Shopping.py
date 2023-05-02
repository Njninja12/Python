
# Week 9 assignment
# Add a that you can add items to and have it display the shaooping cart

print("Welcome! What would you like to do?\n")



choice = ""
item_list = []
price_list = []
while choice != "5":

    menu = ["\n1. Add an Item", "2. Display Cart", "3. Remove Item", "4. Show total", "5. Quit\n"]

    for menu in menu:
        print(menu)

    choice = input("\nPlease type a number --> ")

    if choice == "1":
        item = input("What item would you like to add? ")
        price = float(input("\nWhat is the price of the item? "))
        item_list.append(item)
        price_list.append(price)


    elif choice == "2":
        for i in range(len(item_list)):
            print(f"{i+1}. {item_list[i]} -- {price_list[i]}")


    elif choice == "3":
        index = int(input("Which item would you like to remove? "))
        index = index-1
        if (0 <= index) and (index < len(item_list)):
            del item_list[index]
            del price_list[index]
            print("\nItem removed.\n")
        else:
            print("I'm sorry, but that number isn't on the list.")

    elif choice == "4":
        total = sum(price_list)

        print(f"Total: ${total:.2f}")

    elif choice == "5":

        choice = "5"
    else:
        print("\nPlease choose a number listed\n")

print("\nThanks for shopping with us!!!")

