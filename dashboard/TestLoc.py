import sqlite3
client_id=4
con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()
cursor.execute(""" select name from sqlite_master  where type = "table" """)
rows = cursor.fetchall()
print(rows)
print(type(rows))