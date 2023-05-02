
#t = degrees in fahrenheit
#v = wind speed in mph
#V^0.16 is to the power of .16
#Wind = Wind chill in Farenheit
temp = ""
speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

    # If the temp is in celsius this function converts it
def convert_celsius_to_fahren(c):
    f = (c * 9/5) + 32
    return f
    # This computes the windchill using f as the temperature and v as the wind speed
def compute_wind_chill(f, v):
    wind = 35.74 + 0.6215 * f - 35.75 * v * 0.16 + 0.4275 * t * v * 0.16
    return wind


t = float(input("Please enter your temperature: "))
temp = input("Celsius or Fahrenheit (F/C) ").lower()

if temp == "c":
    f = convert_celsius_to_fahren(t)

elif temp == "f":
    f = t

for v in speed:
    wind = compute_wind_chill(t, v)

    print(f"At temperature {f}F, and wind speed {v}MPH, the windchill is: {wind:.2f}F")

#(wind) = 35.74 + 0.6215*fahren - 35.75(v*0.16) + 0.4275*t(v*0.16)
