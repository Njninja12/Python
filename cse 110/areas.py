square_side = int(input("What is the length of the side? (in cm) "))
area = square_side ** 2
print(f"The area of the square is: {area} cm^2")
print(f"The area of the square is: {area / 10000} m^2")
print()
rectangle_length = int(input("What is the length of the rectangle? (in cm) "))
rectangle_width = int(input("What is the width of the rectangle? (in cm) "))
rec_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rec_area} cm^2")
print(f"The area of the rectangle is: {rec_area / 10000} m^2")
print()
import math
radius = int(input("What is the radius of the circle? (in cm) "))
circle_area = math.pi * radius ** 2
print(f"The area of the circle is: {circle_area} cm^2")
print(f"The area of the circle is: {circle_area / 10000} m^2")