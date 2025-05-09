import sqlite3
conn = sqlite3.connect('./db.sqlite3')
cursor = conn.cursor()
cursor.execute('''delete from website_orders_placed where id=23''')
conn.commit()
cursor.close()
conn.close()
