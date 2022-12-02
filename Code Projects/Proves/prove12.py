# page start
print()

# varaibles
year = 0
year_high = 0
year_low = 0
year_in = 0
country = ""
country_high = ""
country_low = ""
life_list = []
life_list_in = []
life = 0.0
life_high = 0.0
life_low = 500.0
life_ave = 0.0
life_total = 0.0
life_count = 0


# main code

# user input
# year_in = int(input("Enter the year of interest: "))

# page set up
print()

# overall loop
with open("life-expectancy.csv") as life_expectancy:
    for line in life_expectancy:
        info = line.split(",")
        life_list.append(info)

life_list.pop(0)

for sec in life_list:
    life = float(sec[3])
    if life > life_high:
        life_high = life
        country_high = sec[0]
        year_high = int(sec[2])
    elif life < life_low:
        life_low = life
        country_low = sec[0]
        year_low = int(sec[2])

# test
# print(life_list)

# year of intrest
year_in = input("Enter the Year of interet: ")
year_in = int(year_in)

# page set up
print()

# overall max and min
print(
    f"The overall max life expectancy is: {life_high} from {country_high} in {year_high}")
print(
    f"The overall min life expectancy is: {life_low} from {country_low} in {year_low}")

# page set up
print()

# value reset
life_ave = 0
life_high = 0
life_low = 500

# fid year of interest values
for sec in life_list:
    year = int(sec[2])
    if year == year_in:
        life_list_in.append(sec)

for sec in life_list_in:
    life = float(sec[3])
    if life > life_high:
        life_high = life
        country_high = sec[0]
        year_high = int(sec[2])
    elif life < life_low:
        life_low = life
        country_low = sec[0]
        year_low = int(sec[2])

for sec in life_list_in:
    life = float(sec[3])
    life_total += life
    life_count += 1

life_ave = life_total / life_count
life_ave = round(life_ave, 2)

# year of interest min, max, and avearge
print(f"For the year {year_in}:")
print(
    f"""The average life expectancy across all countries was {"{:.2f}".format(life_ave)}""")
print(f"The max life expectancy was in {country_high} with {life_high}")
print(f"The min life expectancy was in {country_low} with {life_low}")

# page end
print()
