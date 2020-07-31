import math

print('What do you want to calculate?')
print('type "n" for the count of months,')
print('type "a" for the annuity monthly payment,')
print('type "p" for credit principal: ')
state = input()
if state == 'n':
    print('Enter credit principal:')
    principal = int(input())
    print('Enter monthly payment:')
    payment = int(input())
    print('Enter credit interest:')
    credit_interest = float(input()) / 100
    i = credit_interest / 12
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    years = n // 12
    months = n - years * 12
    if years == 0 and months > 0:
        print('You need {0} months to repay this credit!'.format(months))
    elif years == 1 and months == 0:
        print('You need 1 year to repay this credit!')
    elif months == 0 and years > 1:
        print('You need {0} years to repay this credit!'.format(years))
    else:
        print('You need {0} years and {1} months to repay this credit!'.format(years, months))
elif state == 'a':
    print('Enter credit principal:')
    principal = int(input())
    print('Enter count of periods:')
    periods = int(input())
    print('Enter credit interest:')
    credit_interest = float(input()) / 100
    i = credit_interest / 12
    annuity_payment = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print('Your annuity payment = {0}!'.format(annuity_payment))
elif state == 'p':
    print('Enter monthly payment: ')
    payment = float(input())
    print('Enter count of periods:')
    months = int(input())
    print('Enter credit interest:')
    credit_interest = float(input()) / 100
    i = credit_interest / 12
    principal = math.floor(payment / ((i * math.pow(1 + i, months)) / (math.pow(1 + i, months) - 1)))
    print('Your credit principal = {0}!'.format(principal))