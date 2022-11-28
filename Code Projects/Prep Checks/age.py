# page start
print()

# varaibles
people = ["Stephanie 36", "John 29", "Emily 24", "Gretchen 54",
          "Noah 12", "Penelope 32", "Michael 2", "Jacob 10"]
age_name = []

# main code
# req 1
for sec in people:
    print(sec)

# page set up
print()

# req 2
for sect in people:
    info = sect.split()
    age_name.append(info)

print(age_name)

# page set up
print()

# req 3 + 4
min_age = 500
min_name = ""
for sect in age_name:
    name = sect[0]
    age = int(sect[1])

    if age < min_age:
        min_age = age
        min_name = name

print(f"the youngest is {min_name} at the age of {min_age}")

# page end
print()
