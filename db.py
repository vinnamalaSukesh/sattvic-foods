import sqlite3
conn = sqlite3.connect('./db.sqlite3')

cursor = conn.cursor()
cursor.execute('DELETE from website_appetizers where item = "" ')
conn.commit()
cursor.close()