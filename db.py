import sqlite3

with sqlite3.connect('./db.sqlite3') as conn:
    cursor = conn.cursor()
    cursor.execute('delete FROM website_orders_placed')
    cursor.execute('SELECT * FROM website_orders_placed')
    orders = cursor.fetchall()
    cursor.close()
    print(orders)

'''cursor = conn.cursor()
cursor.execute('select * from website_appetizers')
Appetizers = cursor.fetchall()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_soups_salads')
Soups_and_salads = cursor.fetchall()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_rice_items')
Rice_items = cursor.fetchall()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_breads_rotis')
Breads_rotis = cursor.fetchall()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_special_curries')
Special_curries = cursor.fetchall()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_side_dishes')
Side_dishes = cursor.fetchall()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_deserts')
Deserts = cursor.fetchall()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_drinks')
Drinks = cursor.fetchall()
cursor.close()'''

