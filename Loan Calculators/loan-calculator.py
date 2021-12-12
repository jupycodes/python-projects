loan_principal = int(input("Enter the loan principal: "))
calc_type = input('''What do you want to calculate?
Type "m" for number of monthly payments,
Type "p" for the monthly payment: ''')
if calc_type == "m":
    monthly_payment = int(input("Enter the monthly payment: "))
    months = loan_principal // monthly_payment
    if loan_principal % monthly_payment != 0:
        months += 1
    print("It will take " + str(months) + " months to pay the loan")
elif calc_type == "p":
    months = int(input("Enter the number of months: "))
    monthly_payment = loan_principal // months
    if loan_principal % monthly_payment == 0:
        print("Your monthly payment = $" + str(monthly_payment))
    else:
        monthly_payment += 1
        last_payment = monthly_payment - (monthly_payment * months - loan_principal)
        print("Your monthly payment = $" + str(monthly_payment) + " and the last payment = $" + str(last_payment))
else:
    print("Invalid Entry")