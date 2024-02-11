#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
from datetime import date
# the current date should be yyyymmdd
print("""1. Add a member
2. Delete a member
3. List all members attended today
4. List all members""")
while True:
    conn = sqlite3.connect('members.db')
    c = conn.cursor()
    current_date = date.today().strftime('%Y%m%d')
    option = input("Option: ")
    if option == '1':
        opt2 = input('Custom ID: ') #IF blank, then it will auto use max_id
        if opt2 == '':
            max_id = c.execute('''SELECT MAX(id) FROM member''')
            max_id = max_id.fetchone()[0] + 1
        else:
            max_id = int(opt2)

        c.execute(f'''INSERT INTO member VALUES ('{max_id}', '{input('Name: ')}', {current_date})''')

    elif option == '2':
        member_id = input('ID: ')
        c.execute(f'''DELETE FROM member WHERE id = {member_id}''')
    elif option == '3':
        members = c.execute(f'''SELECT * FROM member WHERE date = {current_date}''')
        members = members.fetchall()
        for member in members:
            print(f'{member}')
    elif option == '4':
        members = c.execute(f'''SELECT * FROM member''')
        members = members.fetchall()
        for member in members:
            print(f'{member}')
    else:
        exit("Invalid option")
    conn.commit()
    conn.close()

