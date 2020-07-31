import math

print('Enter the credit principal:')
principal = int(input())
print('What do you want to calculate?')
print('type "m" - for the count of months,')
print('type "p" - for the monthly payment:')
action = input()
if action == 'm':
    print('Enter the monthly payment:')
    monthly_payment = int(input())
    months = math.ceil(principal / monthly_payment)
    if months == 1:
        print('It takes 1 month to repay the credit')
    else:
        print('It takes {0} months to repay the credit'.format(months))
elif action == 'p':
    print('Enter the count of months:')
    months = int(input())
    monthly_payment =math.ceil(principal / months)
    lastpayment = math.ceil(principal - (months-1)*monthly_payment)
    if monthly_payment == lastpayment:
        print('Your monthly payment = {0}'.format(monthly_payment))
    else:
        print('Your monthly payment = {0} with last month payment = {1}.'.format(monthly_payment, lastpayment))