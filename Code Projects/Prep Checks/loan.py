# page set up
from operator import truediv


print()

# varables
loan_size = 0
credit_hist = 0
income_size = 0
down_pay_size = 0
loan = False

# main code

# first questions
print("Please answer with a 1 - 10.")
loan_size = int(input("How large is the loan? "))
credit_hist = int(input("How good is your credit history? "))
income_size = int(input("How high is your income? "))
down_pay_size = int(input("How large is your down payment? "))

# loan or no loan
if loan_size >= 5:
    if credit_hist >= 7 and income_size >= 7:
        loan = True
    elif (credit_hist >= 7 or income_size >= 7) and down_pay_size >= 5:
        loan = True
    else:
        loan = False
elif loan_size < 5:
    if credit_hist < 4:
        loan = False
    elif income_size >= 4 and down_pay_size >= 4:
        loan = True
    elif income_size >= 7 or down_pay_size >= 7:
        loan = True
    else:
        loan = False

# the desision
if loan:
    print("You have been aproved for the loan.")
else:
    print("You have been denied access to the loan.")

# page set up
print()
