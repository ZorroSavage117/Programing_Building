# page start
print()

# varaibles
name = ""
position = ""
id_num = ""
salary = ""
employees = []

# main code
# print to screen as is
with open("hr_system.txt") as hr_system:
    for line in hr_system:
        info = line.strip().split()
        employees.append(info)

for sec in employees:
    name = sec[0]
    id_num = sec[1]
    position = sec[2]
    salary = int(sec[3])
    salary = salary / 24
    if position.lower() == "engineer":
        salary += 1000
    print(f"""{name} (ID: {id_num}), {position} - ${"{:.2f}".format(salary)}""")

# page end
print()
