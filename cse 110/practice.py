def convert_celsius_to_fahren(celsius):
    fahren = (celsius * 9/5) + 32
    return fahren


t = float(input("What is the temperature? "))

fahren = convert_celsius_to_fahren(t)

print(fahren)