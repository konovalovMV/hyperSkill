#сбросить последнюю цифру
#умножить нечетную цифру на 2
#вычесть 9 в числа больше 9
#добавить все номера

card_number = '400000997268569'

def LUH(card_number):
    card = [int(num) for num in card_number]
    odd = True
    sum = 0
    for num in card:
        if odd:
            tmp = num * 2
        else:
            tmp = num
        odd = not odd
        if tmp > 9:
            tmp -= 9
        sum +=tmp
    if sum % 10 == 0:
        return '0'
    else:
        return str(10 - (sum % 10))

print(LUH(card_number))