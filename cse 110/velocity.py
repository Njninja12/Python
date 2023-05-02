print("Welcome to the Velocity Calculator! Please Enter the Following:")
print()


m = float(input("Mass (in Kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): \n"))

import math

print()
c = (1 / 2) * p * A * C
print(f"The inner value of c is: {c:.3f}")
V = math.sqrt(m*g/c) * (1-math.exp((-math.sqrt(m*g/c)/m)*t))
print(f"The velocity after {t:.3f} seconds is: {V:.3f} m/s")

v_terminal = math.sqrt((m*g)/c)
print(f"The object's terminal velocity is {v_terminal:.3f} m/s")