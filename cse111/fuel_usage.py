def main():
    # Get an odometer value in U.S. miles from the user.
    odom_1 = int(input("Please enter your starting odometer: "))
    # Get another odometer value in U.S. miles from the user.
    odom_2 = int(input("Please enter your ending odometer: "))
    # Get a fuel amount in U.S. gallons from the user.
    fuel_amount = float(input("Please enter the fuel used (in U.S. gallons): "))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(odom_1, odom_2, fuel_amount)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon.")
    print(f"{lp100k:.2f} liters per 100 kilometers.")



def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel."""
    mpg = abs(end_miles - start_miles) / amount_gallons
    """Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value."""
    lp100k = 235.215 / mpg
    """Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return lp100k


# Call the main function so that
# this program will start executing.
main()