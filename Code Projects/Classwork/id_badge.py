# page set up
print()

# vairables
first_name = "unknown"
last_name = "unknown"
job_title = "unknown"
id_number = "unknown"
email = "unknown"
phone = "unknown"

# main code
print("Please enter the following imformation:\n")
first_name = input("First name:  ")
last_name = input("Last name:  ")
email = input("Email address:  ")
phone = input("Phone number:  ")
job_title = input("Job title:  ")
id_number = input("ID Number:  ")

print("\nThe ID Card is:\n----------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}\n")
print(email.lower())
print(phone)
print("----------------------------------------")

# page set up
print()
