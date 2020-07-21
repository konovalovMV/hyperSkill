import random
def print_menu(session):
    if session:
        print('1. Balance')
        print('2. Log out')
    else:
        print('1. Create an account')
        print('2. Log into account')
    print('0. Exit')

def card_creater():
    account_number = ''
    for _ in range(9):
        account_number += str(random.randint(0, 9))
    check_sum = str(random.randint(0, 9))
    card_number = '400000' + account_number + check_sum
    print('Your card number:')
    print(card_number)
    PIN  = ''
    for _ in range(4):
        PIN += str(random.randint(0, 9))
    print('Your card PIN:')
    print(PIN)
    return {card_number:PIN}

def authorization(cards):
    print('Enter your card number:')
    card_number = input()
    print('Enter your PIN:')
    PIN = input()
    if card_number in cards:
        card_info = cards.get(card_number)
        if card_info[0] is PIN:
            return True
    return False

session = False
while(True):
    cards = {}
    print_menu(session)
    command = input()
    if command is '0':
        print('Bye!')
        break
    if command is '1':
        print('Your card has been created')
        new_card = card_creater()
        cards.update(new_card)
    if command is '2':
        if authorization(cards):
            print('You have successfully logged in!')
            session = True
        else:
            print('Wrong card number or PIN!')
