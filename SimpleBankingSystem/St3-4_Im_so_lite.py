# Write your code here
import random
import sqlite3

SHOW_TABLE_NAME_QUERY = 'SELECT name FROM sqlite_master WHERE type ="table" AND name NOT LIKE "sqlite_%";'
CREATE_CARD_TABLE_QUERY = 'create table card(id integer PRIMARY KEY AUTOINCREMENT NOT NULL, number text, pin text, balance integer default 0)'
INSERT_CARD_QUERY = "insert into card (number, pin) values ('{0}', '{1}')"
SELECT_CARD_QUERY = 'SELECT * FROM card where number = {0} and pin = {1}'
def print_menu(session):
    if session:
        print('1. Balance')
        print('2. Log out')
    else:
        print('1. Create an account')
        print('2. Log into account')
    print('0. Exit')
    
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

def card_creater():
    account_number = ''.join([str(random.randint(0,9)) for _ in range(9)])
    card_number = '400000' + account_number
    checksum = LUH(card_number)
    card_number += checksum
    PIN  = ''.join([str(random.randint(0,9)) for _ in range(4)])
    return [card_number, PIN]


session = False
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute(SHOW_TABLE_NAME_QUERY)
result = cur.fetchall() 
if len(result) == 0:
    cur.execute(CREATE_CARD_TABLE_QUERY)
    conn.commit()


while(True):
    print_menu(session)
    command = input()
    print()
    if command == '0': #exit
        print('Bye!')
        break
    if not session and command == '1': #registration
        print('Your card has been created')
        new_card=card_creater()
        number = new_card[0]
        pin = new_card[1]
        print('Your card number:', new_card[0], 'Your card PIN:', new_card[1], sep='\n')
        print()
        cur.execute(INSERT_CARD_QUERY.format(new_card[0], new_card[1]))
        conn.commit()


    if not session and command == '2': #log in
        print('Enter your card number:')
        card_number = input()
        print('Enter your PIN:')
        pin = input()
        print()
        cur.execute(SELECT_CARD_QUERY.format(card_number, pin))
        result = cur.fetchall()
        if len(result) == 0:
            print('Wrong card number or PIN!')
            print()
        else:
            print('You have successfully logged in!')
            print()
            session = True
            continue
    if session and command == '1': #print balanse
        print('Balance:', 0)
        print()
    if session and command == '2': #log out
        print('You have successfully logged out!')
        print()
        session = False


