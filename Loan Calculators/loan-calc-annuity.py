import math

calc_type = input('''What do you want to calculate?
Type "n" for number of monthly payments,
Type "a" for annuity monthly payment amount,
Type "p" for loan principal: ''')

if calc_type == "n":
    loan_principal = int(input("Enter the loan principal: "))
    payment = float(input("Enter the monthly payment: "))
    interest = float(input("Enter the loan interest: "))
    i = interest / (12 * 100)
    months = math.ceil(math.log(payment / (payment - i * loan_principal), i + 1))
    years = months // 12
    months = months % 12
    print("it will take {0} years and {1} months to repay this loan!".format(years,months))
elif calc_type == "a":
    loan_principal = int(input("Enter the loan principal: "))
    months = int(input("Enter the number of periods: "))
    interest = float(input("Enter the loan interest: "))
    i = interest / (12 * 100)
    payment = math.ceil(loan_principal * i * (i+1)**months / ((i+1)**months - 1))
    print("Your monthly payment = {}!".format(payment))
elif calc_type == "p":
    payment = float(input("Enter the annuity payment: "))
    months = int(input("Enter the number of periods: "))
    interest = float(input("Enter the loan interest: "))
    i = interest / (12 * 100)
    loan_principal = round(payment / (i * (i+1)**months / ((i+1)**months - 1)))
    print("Your loan principal = {}!".format(loan_principal))
else:
    print("Incorrect input")
