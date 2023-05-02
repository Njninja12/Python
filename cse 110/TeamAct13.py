import math


def compute_area(length,height):
    area = length * height
    return area

def compute_area_circle(radius):
    area_circle = math.pi * radius ** 2
    return area_circle

square_length = float(input("What is the length of the square? "))
square_heigth = square_length
square_area = compute_area(square_length, square_heigth)
print(f"The square area is: {square_area}")

retangle_length = float(input("What is the length of the retangle? "))
retangle_heigth = float(input("What is the heigth of the retangle? "))
retangle_area = compute_area(retangle_length, retangle_heigth)
print(f"The retangle area is: {retangle_area}")

circle_radius = float(input("What is the radius of the circle? "))
area_circle = compute_area_circle(circle_radius)
print(f"The square area is: {area_circle}")