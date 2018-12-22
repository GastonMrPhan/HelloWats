import sqlite3
client_id=(4,)
con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()
cursor.execute("SELECT * FROM dashboard_conso_eur WHERE client_id = ?",client_id)
rows = cursor.fetchall()
print(rows)
print(type(rows))