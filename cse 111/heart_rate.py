"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = int(input("What is your age: "))

max_heart_rate = 220 - age

low_strength = max_heart_rate * .65
high_strength = max_heart_rate * .85

print("When working out to strengthen your heart, try to keep")
print(f"your heart rate between {low_strength:.0f} and {high_strength:.0f} beats per minute.")