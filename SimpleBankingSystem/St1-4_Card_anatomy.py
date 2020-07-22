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
    account_number = ''.join([str(random.randint(0,9)) for _ in range(9)])
    check_sum = str(random.randint(0, 9))
    card_number = '400000' + account_number + check_sum
    PIN  = ''.join([str(random.randint(0,9)) for _ in range(4)])
    return [card_number, PIN]

session = False
cards = {}
while(True):
    print_menu(session)
    command = input()
    print()
    if command is '0': #exit
        print('Bye!')
        break
    if not session and command is '1': #registration
        print('Your card has been created')
        new_card=card_creater()
        print('Your card number:', new_card[0], 'Your card PIN:', new_card[1], sep='\n')
        print()
        cards.update({new_card[0]:[new_card[1], 0]})
    if not session and command is '2': #log in
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        pin = input()
        print()
        if card_number in cards:
            card_info = cards.get(card_number)
            if pin == card_info[0]:
                print('You have successfully logged in!')
                session = True
            else:
                print('Wrong card number or PIN!')
        else:
            print('Wrong card number or PIN!')
    if session and command is '1': #print balanse
        print('Balance:', card_info[1])
        print()
    if session and command is '2': #log out
        print('You have successfully logged out!')
        print()
        session = False


