shopping_list = []
run = ""

print("Please enter the items in your shopping list. (Type quit when finished) ")

while run != "quit":
    item = input("Item: ").lower()
    if item != "quit":
        shopping_list.append(item)
    else:
        run = "quit"
        print("\nThe shopping list items are:")
        for items in shopping_list:
            print(f"{items}")

