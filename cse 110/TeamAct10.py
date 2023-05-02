accounts = []
balances = []

is_adding = "true"

print("Please enter the name of your account and balance. (Type quit when done.)")

while is_adding != "quit":
    account = input("What is the name of your account? ")
    if account != "quit":
        accounts.append(account)
        balance = float(input("What is the balance of the account? "))
        balances.append(balance)

    
