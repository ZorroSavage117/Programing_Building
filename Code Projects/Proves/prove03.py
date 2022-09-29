# page set up
import math
print()

# variables
meal_child = 0.00
meal_adult = 0.00
num_child = 0
num_adult = 0
tax_rate = 0.00
tip = ""
tip_rate = 0.00
tip_amount = 0.00
subtotal = 0.00
sales_tax = 0.00
total = 0.00
payment = 0.00
change = 0.00

# main code
meal_child = float(input("What is the price of a child's meal? "))
meal_adult = float(input("What is the price of an adult's meal? "))
num_child = int(input("How many children are there? "))
num_adult = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
tip = input("Whould you like to leave a tip? ")

if tip.lower() == "yes" or tip.lower() == "y":
    tip_rate = float(input("What is the tip rate? "))
    tip_rate = tip_rate / 100

tax_rate = tax_rate / 100
subtotal = (meal_child * num_child) + (meal_adult * num_adult)
sales_tax = subtotal * tax_rate
tip_amount = subtotal * tip_rate
total = subtotal + sales_tax + tip_amount
subtotal = round(subtotal, 2)
sales_tax = round(sales_tax, 2)
tip_amount = round(tip_amount, 2)
total = round(total, 2)

print()
print(f"""Subtotal: ${"{:.2f}".format(subtotal)}
Sales Tax: ${"{:.2f}".format(sales_tax)}
Tip Ammount: ${"{:.2f}".format(tip_amount)}
Total: ${"{:.2f}".format(total)}""")

print()
payment = float(input("What is the payment amount? "))
change = payment - total
change = round(change, 2)
print(f"""Change: ${"{:.2f}".format(change)}""")

# page set up
print()
