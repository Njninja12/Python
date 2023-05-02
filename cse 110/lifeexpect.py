
choice = input("What is the country of interest? ").lower()

max_life = -1
min_life = 1000
min_country = ""
max_country = ""
overall_max = -1
overall_min = 1000
overall_max_country = ""
overall_min_country = ""
# Set the total life and amount to zero so it will always add
# the first line of the file first.
total_life = 0
amount = 0



with open("life-expectancy.csv") as life_expect:
    next(life_expect)
    for line in life_expect:
        parts = line.split(",")
        country = parts[0].strip()
        code = parts[1].strip()
        year = int(parts[2])
        life = float(parts[3])

        if life > overall_max:
            overall_max = life
            overall_max_country = country
        if life < overall_min:
            overall_min = life
            overall_min_country = country



        if country.lower() == choice:

            #This will add the life expectancy for every count and keep a count
            #of how many countries are in that year.
            total_life += life
            amount += 1


            if life > max_life:
                max_life = life
                max_country = country

            if life < min_life:
                min_life = life
                min_country = country

    #Here it finally calculates the average by using the variables above.
    average = total_life/amount
    


    
    print(f"The overall max life expectancy is in {overall_max_country} and is {overall_max}.")
    print(f"The overall min life expectancy is in {overall_min_country} and is {overall_min}.")
    print(f"\nFor the year {choice}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The maximum life expectancy was in {max_country} with {max_life}")
    print(f"The minimum life expectancy was in {min_country} with {min_life}")
