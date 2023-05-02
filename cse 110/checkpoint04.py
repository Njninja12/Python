#Fahrenheit to Celsius calulator
F_temp = float(input("What is the temperature (in Fahrenheit): "))

C_temp = ((F_temp - 32) * (5 / 9))
print(f"The temperature in Celsius is {C_temp:.1f}")