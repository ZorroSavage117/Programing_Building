# page set up
print()

# Variables
age = "unknown"
cartons = "unknown"
eggs = 0
cookies = "unknown"
people = "unknown"
amount = 0.01

# main code
age = input("How old are you? ")
age = int(age)
age = age + 1
print(f"On your next berthday, you will be {age}\n")
cartons = input("How many egg cartons do you have? ")
cartons = int(cartons)
eggs = cartons * 12
print(f"You have {eggs} eggs\n")
cookies = input("How many cookies do you have? ")
people = input("How many people are there? ")
cookies = float(cookies)
people = float(people)
amount = cookies / people
print(f"Each person may have {amount} cookies")

# page set up
print()
