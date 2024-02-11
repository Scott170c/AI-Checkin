#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('members.db')
c = conn.cursor()
# create table: id, name, date
c.execute('''CREATE TABLE member (id key, name text, date text)''')
conn.commit()
conn.close()