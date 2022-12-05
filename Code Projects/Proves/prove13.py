# page start
print()

# varaibles
temp_in = 0
vec = 0
chill = 0.0
far_cel = ""

# functions


def cal_chill(t, v):
    chill = (35.74 + (0.6215 * t) - (35.75 * (v ** 0.16)) +
             (0.4275 * t * (v ** 0.16)))
    # print(chill)
    print(
        f"""At temperature {t}.0F, and wind speed {v} mph, the windchill is: {"{:.2f}".format(chill)}F""")


def cal_far(t):
    global temp_in
    temp_in = int((t * (9 / 5)) + 32)


# main code
# inputs
temp_in = int(input("What is the temperature? "))
far_cel = input("Fahrenheit or Celsius (F/c)? ")

if far_cel == "C":
    cal_far(temp_in)

# outputs
while vec <= 55:
    vec += 5
    cal_chill(temp_in, vec)


# page end
print()
