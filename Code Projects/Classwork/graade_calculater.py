# page set up
print()

# variables
grade_percent = 0
last_dig = 0
leter_grade = ""
grade_half = ""
passing = ""
outcome = ""

# main code
# user input
grade_percent = int(input("What is your grade percetage? "))

# calculation
last_dig = grade_percent % 10

# if statements

# letter grade
if grade_percent >= 90:
    leter_grade = "A"
    passing = "y"
elif grade_percent >= 80:
    leter_grade = "B"
    passing = "y"
elif grade_percent >= 70:
    leter_grade = "C"
    passing = "y"
elif grade_percent >= 60:
    leter_grade = "D"
    passing = "n"
else:
    leter_grade = "F"
    passing = "n"

# is it + or -
if last_dig >= 7:
    grade_half = "+"
elif last_dig < 3:
    grade_half = "-"
else:
    grade_half = ""

# there is no A+
if leter_grade == "A" and grade_half == "+" or grade_percent >= 100:
    grade_half = ""

# there is no F+ or F-
if leter_grade == "F":
    grade_half = ""

# are they passing and what should I say to them
if passing == "y":
    outcome = "Congadulations, you are passing."
else:
    outcome = "Keep trying, you got this."

# output
print(f"""You have a(n) {leter_grade}{grade_half}. {outcome}""")


# page set up
print()
