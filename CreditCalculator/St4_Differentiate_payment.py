import math
import sys

args = sys.argv
args.pop(0)
args_dict = {}
try:
    for arg in args:
        tmp = arg.split('=')
        args_dict.update({tmp[0]: tmp[1]})

    if len(args_dict) < 4:
        raise SyntaxError

    if '--type' in args_dict:
        if args_dict['--type'] == 'diff':
            if '--payment' in args_dict:
                raise SyntaxError
            p = int(args_dict['--principal'])
            n = int(args_dict['--periods'])
            i = float(args_dict['--interest'])
            if p < 0 or n < 0 or i < 0 :
                raise SyntaxError
            i = i / (12 * 100)
            t = 0
            for m in range(n):
                m += 1
                D = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
                print('Month {0}: paid out {1}'. format(m, D))
                t += D
            print()
            print('Overpayment = {0}'.format(t - p))
        elif args_dict['--type'] == 'annuity':
            if '--principal' in args_dict and '--periods' in args_dict and '--interest' in args_dict:
                p = int(args_dict['--principal'])
                n = int(args_dict['--periods'])
                i = float(args_dict['--interest'])
                if p < 0 or n < 0 or i < 0 :
                    raise SyntaxError
                i = i / (12 * 100)
                A = math.ceil(p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
                print('Your annuity payment = {0}!'.format(A))
                print('Overpayment = {0}'.format(A * n - p))
            elif '--payment' in args_dict and '--periods' in args_dict and '--interest' in args_dict:
                a = int(args_dict['--payment'])
                n = int(args_dict['--periods'])
                i = float(args_dict['--interest'])
                if a < 0 or n < 0 or i < 0 :
                    raise SyntaxError
                i = i / (12 * 100)
                p = math.floor(a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
                print('Your credit principal = {0}!'.format(p))
                print('Overpayment = {0}'.format(a * n - p))
            elif '--principal' in args_dict and '--payment' in args_dict and '--interest' in args_dict:
                a = int(args_dict['--payment'])
                p = int(args_dict['--principal'])
                i = float(args_dict['--interest'])
                if a < 0 or p < 0 or i < 0 :
                    raise SyntaxError
                i = i / (12 * 100)
                n = math.ceil(math.log(a / (a - i * p), 1 + i))
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
                print('Overpayment = {0}'.format(a * n - p))
            else:
                raise SyntaxError
        else:
            raise SyntaxError
    else:
        raise SyntaxError
except SyntaxError:
    print('Incorrect parameters')
except Exception:
    print('Incorrect parameters')