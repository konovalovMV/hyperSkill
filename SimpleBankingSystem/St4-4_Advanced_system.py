# Write your code here
import random
import sqlite3

SHOW_TABLE_NAME_QUERY = 'SELECT name FROM sqlite_master WHERE type ="table" AND name NOT LIKE "sqlite_%";'
CREATE_CARD_TABLE_QUERY = 'create table card(id integer PRIMARY KEY AUTOINCREMENT NOT NULL, number text, pin text, balance integer default 0)'
INSERT_CARD_QUERY = "insert into card (number, pin) values ('{0}', '{1}')"
SELECT_CARD_QUERY = 'SELECT * FROM card where number = {0} and pin = {1}'
ADD_INCOME_QUERY = 'UPDATE card SET balance = {0} where number = {1}'
DELETE_CARD_QUERY = 'DELETE FROM card WHERE number = {0}'
TRANSFER_MONEY_SELECT_QUERY = 'SELECT * FROM card where number = {0}'

def print_menu(session):
    if session:
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
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
card_number = 0
balance = 0
while(True):
    print_menu(session)
    command = input()
    print()
    if command == '0': #exit
        print('Bye!')
        break
    if session:
        if command == '1': #print balanse
            print('Balance:', balance, end='\n\n')
        elif command == '2': #Add income
            print('Enter income:')
            add = int(input())
            balance += add
            cur.execute(ADD_INCOME_QUERY.format(balance, card_number))
            conn.commit()
            print('Income was added!', end='\n\n')
        elif command == '3': #do transfer
            print('Transfer')
            print('Enter card number:')
            transfer_card = input()
            if transfer_card[15:] != LUH(transfer_card[:15]):
                print('Probably you made mistake in the card number. Please try again!', end='\n\n')
                continue
            if transfer_card == card_number:
                print("You can't transfer money to the same account!")
                continue
            cur.execute(TRANSFER_MONEY_SELECT_QUERY.format(transfer_card))
            result = cur.fetchone()
            if not result:
                print('Such a card does not exist.', end='\n\n')
            else:
                print('Enter how much money you want to transfer:')
                transfer_money = int(input())
                if transfer_money > balance:
                    print('Not enough money!', end='\n\n')
                    continue
                else:
                    transfer_money += result[3]
                    cur.execute(ADD_INCOME_QUERY.format(transfer_money, transfer_card))
                    balance -= transfer_money
                    cur.execute(ADD_INCOME_QUERY.format(balance, card_number))
                    conn.commit()
                    print('Success!', end='\n\n')
        elif command == '4': #close account
            cur.execute(DELETE_CARD_QUERY.format(card_number))
            conn.commit()
            print('The account has been closed!', end='\n\n')
            session = False
        elif command == '5': #log out
            print('You have successfully logged out!', end='\n\n')
            session = False
    else:
        if command == '1': #registration
            print('Your card has been created')
            new_card = card_creater()
            print('Your card number:', new_card[0], 'Your card PIN:', new_card[1], sep='\n')
            print()
            cur.execute(INSERT_CARD_QUERY.format(new_card[0], new_card[1]))
            conn.commit()
        elif command == '2': #log in
            print('Enter your card number:')
            card_number = input()
            print('Enter your PIN:')
            pin = input()
            print()
            cur.execute(SELECT_CARD_QUERY.format(card_number, pin))
            result = cur.fetchone()
            if result:
                print('You have successfully logged in!', end='\n\n')
                session = True
                balance = result[3]
            else:
                print('Wrong card number or PIN!', end='\n\n')