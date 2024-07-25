from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
conn = sqlite3.connect('./db.sqlite3')

cursor = conn.cursor()
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
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from website_orders_placed')
orders = cursor.fetchall()
cursor.close()

app = QApplication([])
window = QWidget()
window.setFixedSize(1350,680)
window_layout = QGridLayout()
title = QLabel('Sattvic Foods')
title.setFixedHeight(30)
title.setStyleSheet("font-size:30px; color:rgb(0,30,0);")
title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

tab1 = QPushButton('Edit menu',clicked = lambda checked, tab='menu':change_tab(tab))
tab1.setStyleSheet("color:white;background-color:black;font-size:16px;font-weight:900;")
tab2 = QPushButton('View orders',clicked = lambda checked, tab='orders':change_tab(tab))
tab2.setStyleSheet("color:white;background-color:black;font-size:16px;font-weight:900;")
tab1.setFixedWidth(663)
tab2.setFixedWidth(663)

tab3 = QPushButton('Orders Completed',clicked = lambda checked, tab='completed':switch_tab(tab))
tab3.setStyleSheet("color:white;background-color:black;font-size:16px;font-weight:900;")
tab4 = QPushButton('Orders Pending',clicked = lambda checked,tab='pending':switch_tab(tab))
tab4.setStyleSheet("color:white;background-color:black;font-size:16px;font-weight:900;")
tab3.setFixedWidth(663)
tab4.setFixedWidth(663)

def change_tab(tab):
    global orders_box,tab3,tab4
    if(tab == 'orders'):
        categories[curr_cat].hide()
        buttons.hide()
        separator.hide()
        window_layout.removeWidget(categories[curr_cat])
        window_layout.removeWidget(separator)
        window_layout.removeWidget(buttons)
        window_layout.addWidget(tab4,2,0,1,3)
        window_layout.addWidget(tab3,2,3,1,3)
        window_layout.addWidget(pending_orders,3,0,2,6)
        tab3.show()
        tab4.show()
        pending_orders.show()
    else:
        tab3.hide()
        tab4.hide()
        window_layout.removeWidget(tab3)
        window_layout.removeWidget(tab4)
        pending_orders.hide()
        window_layout.removeWidget(pending_orders)
        window_layout.removeWidget(comp_orders)
        comp_orders.hide()

        window_layout.addWidget(buttons,2,0,3,1)
        window_layout.addWidget(separator,2,1,3,1)
        window_layout.addWidget(categories[curr_cat],2,2,3,4)
        categories[curr_cat].show()
        buttons.show()
        separator.show()

def Items(category):
    items_box = QGroupBox()
    items = QVBoxLayout()
    box = QGroupBox()
    card = QHBoxLayout()
    box.setLayout(card)
    add = QPushButton('ADD NEW ITEM')
    add.clicked.connect(add_item)
    add.setFixedWidth(200)
    add.setStyleSheet("font-size:20px;color:white;border:2px solid rgb(0,0,50);border-radius:5px;background-color:#a52a2a;")
    card.addWidget(add)
    items.addWidget(box)

    box = QGroupBox()
    card = QHBoxLayout()
    box.setLayout(card)
    l1 = QLabel('ID')
    l1.setFixedWidth(30)
    l1.setFixedHeight(20)
    l1.setStyleSheet("font-size:16px; color:red;")
    l1.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    card.addWidget(l1)

    l2 = QLabel('Item name')
    l2.setFixedWidth(250)
    l2.setFixedHeight(20)
    l2.setStyleSheet("font-size:16px; color:red;")
    l2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    card.addWidget(l2)

    l3 = QLabel('Price')
    l3.setFixedWidth(100)
    l3.setFixedHeight(20)
    l3.setStyleSheet("font-size:16px; color:red;")
    l3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    card.addWidget(l3)
    l4 = QLabel('Path')
    l4.setFixedWidth(250)
    l4.setFixedHeight(20)
    l4.setStyleSheet("font-size:16px; color:red;")
    l4.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    card.addWidget(l4)
    l5 = QLabel("Availability")
    l5.setStyleSheet("font-size:16px; color:red;")
    l5.setFixedWidth(100)
    l5.setFixedHeight(20)
    l6 = QLabel("")
    l6.setFixedWidth(80)
    l6.setFixedHeight(20)
    l7 = QLabel("")
    l7.setFixedWidth(80)
    l7.setFixedHeight(20)
    card.addWidget(l5)
    card.addWidget(l6)
    card.addWidget(l7)

    items.addWidget(box)

    for i in category:
        box = QGroupBox()
        card = QHBoxLayout()
        box.setLayout(card)

        id_ = QLabel(str(i[0]))
        id_.setFixedWidth(30)
        id_.setStyleSheet("font-size:16px;")
        card.addWidget(id_)

        name = QLineEdit()
        name.setFixedWidth(250)
        name.setStyleSheet("font-size:14px; ")
        name.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        name.setText(str(i[1]))
        name.setReadOnly(True)
        card.addWidget(name)

        price = QLineEdit()
        price.setFixedWidth(100)
        price.setStyleSheet("font-size:14px;")
        price.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        price.setText(str(i[2]))
        price.setReadOnly(True)
        card.addWidget(price)

        path = QLineEdit()
        path.setFixedWidth(250)
        path.setStyleSheet("font-size:14px; ")
        path.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        path.setText(str(i[3]))
        path.setReadOnly(True)
        card.addWidget(path)

        Cbox = QComboBox()
        Cbox.addItems(['Available','Unavailable','Delete'])
        Cbox.setStyleSheet("font-size:14px;")
        Cbox.setEnabled(False)
        Cbox.setFixedWidth(100)
        card.addWidget(Cbox)

        entries = [name,price,path]
        edit = QPushButton('EDIT',clicked = lambda checked,Sno=id_,entries=entries,cbox=Cbox:Edit(Sno,entries,cbox))
        edit.setStyleSheet("background-color:rgb(0,0,70); color:white; font-size:16px; border-radius:2px;")
        edit.setFixedWidth(80)
        card.addWidget(edit)

        save = QPushButton('SAVE',clicked = lambda checked,Sno=id_,entries=entries,cbox=Cbox,p_layout=items:Save(Sno,entries,cbox,p_layout))
        save.setStyleSheet("background-color:rgb(0,30,0); color:white;font-size:16px; border-radius:2px;")
        save.setFixedWidth(80)
        card.addWidget(save)

        box.setStyleSheet("height:30px;")
        items.addWidget(box)

    items_box.setLayout(items)
    scroll_bar = QScrollArea()
    scroll_bar.setWidgetResizable(True)
    scroll_bar.setWidget(items_box)
    return scroll_bar

def add_item():
    global curr_cat
    popup = QDialog()
    popup.setWindowTitle(f'Add new item to {curr_cat}')
    popup_layout = QVBoxLayout()
    popup.setLayout(popup_layout)

    name = QLineEdit()
    name.setFixedSize(300,30)
    name.setStyleSheet("font-size:16px;")
    name.setPlaceholderText('Name')
    popup_layout.addWidget(name)

    price = QLineEdit()
    price.setFixedSize(300,30)
    price.setPlaceholderText('Price')
    price.setStyleSheet("font-size:16px;")
    popup_layout.addWidget(price)

    path = QLineEdit()
    path.setFixedSize(300,30)
    path.setPlaceholderText('Img Path')
    path.setStyleSheet("font-size:16px;")
    popup_layout.addWidget(path)

    availability = QComboBox()
    availability.addItems(['Available','Unavailable'])
    availability.setStyleSheet("font-size:16px;")
    availability.setFixedSize(300,30)
    popup_layout.addWidget(availability)

    button = QPushButton('SAVE')
    button.setStyleSheet("font-size:20px;color:white;background-color:rgb(0,50,0);")
    button.setFixedSize(100,30)
    button.clicked.connect(lambda checked,item=name,price=price,path=path,availability=availability.currentText():save_add_item(item,price,path,availability))

    button_layout = QHBoxLayout()
    button_layout.addStretch()
    button_layout.addWidget(button)
    button_layout.addStretch()
    popup_layout.addLayout(button_layout)

    popup_layout.setSpacing(15)
    popup.exec()

def save_add_item(item,price,path,availability):
    name = item.text()
    price = price.text()
    path = path.text()
    table = 'website_' + curr_cat
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO {table} (item,price,img,availability)  VALUES (?, ?, ?, ?)''', (name,price,path,availability))
    conn.commit()
    cursor.close()
    dialog = item.parent()
    dialog.close()

def Edit(id_,entries,cbox):
    for entry in entries:
        entry.setReadOnly(False)
    entries[1].setFocus()
    cbox.setEnabled(True)

def Save(id_,entries,cbox,p_layout):
    global curr_cat
    availability = cbox.currentText()
    if(availability == 'Delete'):
        table = 'website_' + curr_cat
        cursor = conn.cursor()
        cursor.execute(f'''DELETE from {table} WHERE id = ?;''', (id_.text()))
        conn.commit()
        cursor.close()
        cbox.parent().hide()
        p_layout.removeWidget(cbox.parent())
    else:
        for entry in entries:
            entry.setReadOnly(True)
        id_ = id_.text()
        name = entries[0].text()
        price = entries[1].text()
        path = entries[2].text()
        availability = cbox.currentText()
        for entry in entries:
            entry.setReadOnly(True)
        cbox.setEnabled(False)
        table = 'website_' + curr_cat
        cursor = conn.cursor()
        cursor.execute(f'''UPDATE {table}
                        SET item = ?, price = ?, img = ?, availability = ?
                        WHERE id = ?;''', (name, price, path, availability, id_))
        conn.commit()
        cursor.close()

i = 0
def switch_item(button):
    global layout,i,cards_layout
    parent = button.parent()
    window_layout.removeWidget(parent)
    x = i // 4
    y = i % 4
    layout.addWidget(parent,x,y)
    i += 1
    widgets = []
    for row in range(cards_layout.rowCount()):
        for col in range(cards_layout.columnCount()):
            item = cards_layout.itemAtPosition(row,col)
            if(item is not None):
                item = item.widget()
                widgets.append(item)
                cards_layout.removeWidget(item)
                item.hide()
    x = 0
    y = 0
    for k in range(len(widgets)):
        cards_layout.addWidget(widgets[k],x,y)
        widgets[k].show()
        y += 1
        if(y == 4):
            x += 1
            y = 0

def show_info(name,Cno,address):
    popup = QDialog()
    popup_layout = QVBoxLayout()
    popup.setWindowTitle('Customer details')
    popup.setLayout(popup_layout)
    t = 'customer name : ' + name
    label = QLabel(t)
    label.setStyleSheet("font-size:16px;")
    popup_layout.addWidget(label)

    t = 'Contact No : ' + Cno
    label = QLabel(t)
    label.setStyleSheet("font-size:16px;")
    popup_layout.addWidget(label)

    t = 'Address : ' + address
    label = QLabel(t)
    label.setStyleSheet("font-size:16px;")
    popup_layout.addWidget(label)
    popup.exec()

def Orders_placed():
    cards = QGroupBox()
    cards.setStyleSheet("background-color:white;")
    global cards_layout
    cards_layout = QGridLayout()
    cards.setLayout(cards_layout)
    cards.setFixedWidth(1300)
    x = 0
    y = 0
    for order in orders:
        card = QGroupBox()
        layout = QVBoxLayout()
        card.setLayout(layout)
        card.setStyleSheet("background-color:white;")
        card.setFixedSize(295,350)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(0, 0, 0, 160))
        card.setGraphicsEffect(shadow)

        title = QGroupBox()
        title_layout = QHBoxLayout()
        title.setLayout(title_layout)

        label = QLabel(str(order[0]))
        label.setStyleSheet("font-size:20px;border:2px solid red;border-radius:50%;")
        label.setFixedSize(30,20)
        title_layout.addWidget(label)

        t = 'Order placed at : ' + str(order[3].split(' ')[1])
        label = QLabel(t)
        label.setStyleSheet("font-size:18px;color:red;")
        label.setFixedHeight(20)
        label.setAlignment(Qt.AlignRight | Qt.AlignTop)
        title_layout.addWidget(label)

        layout.addWidget(title)
        layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Minimum))

        items = QGroupBox()
        items_layout = QVBoxLayout()
        items.setLayout(items_layout)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(200)
        scroll.setWidget(items)

        price = 0
        for i in order[2].split(';'):
            item = i.split(',')
            t = item[0] + '  (' + item[2] + ')'
            label = QLabel(t)
            label.setStyleSheet("font-size:18px;")
            label.setFixedHeight(30)
            price += int(item[1])
            items_layout.addWidget(label)

        layout.addWidget(scroll)
        t = 'Price : ' + str(price)
        label = QLabel(t)
        label.setFixedHeight(20)
        label.setStyleSheet("font-size:18px;color:red;")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addWidget(label)
        user = QPushButton('User details')
        completed = QPushButton('Completed')
        completed.clicked.connect(lambda _, b=completed: switch_item(b))
        layout.addWidget(user)
        user.setFixedHeight(25)
        completed.setFixedHeight(25)
        user.clicked.connect(lambda checked,name=order[1],Cno=order[4],address=order[5]:show_info(name,Cno,address))
        user.setStyleSheet("border:2px solid white;font-size:18px;color:white;background-color:rgb(0,0,50);")
        completed.setStyleSheet("border:2px solid white;font-size:18px;color:white;background-color:rgb(0,50,0);")
        layout.addWidget(completed)

        cards_layout.addWidget(card,x,y)
        y += 1
        if(y == 4):
            x += 1
            y = 0
    scroll_bar = QScrollArea()
    scroll_bar.setWidgetResizable(True)
    scroll_bar.setWidget(cards)
    return scroll_bar
pending_orders = Orders_placed()

def switch_tab(tab):
    if(tab == 'completed'):
        pending_orders.hide()
        comp_orders.show()
        window_layout.removeWidget(pending_orders)
        window_layout.addWidget(comp_orders,3,0,2,6)
    else:
        window_layout.removeWidget(comp_orders)
        comp_orders.hide()
        window_layout.addWidget(pending_orders,3,0,2,6)
        pending_orders.show()

def completed_orders():
    com_order = QGroupBox()
    global layout
    layout = QGridLayout()
    com_order.setLayout(layout)
    return com_order
comp_orders = completed_orders()

global curr_cat
curr_cat = 'appetizers'

buttons = QGroupBox()
b_layout = QVBoxLayout()
buttons.setLayout(b_layout)
buttons.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
def menu_button(category):
    button = QPushButton(category,clicked = lambda checked, cat=category:change_category(cat))
    button.setStyleSheet("color:rgb(0, 0, 50);font-size:18px;width:250px; margin:0 20px;font:Courier")
    button.setFixedWidth(250)
    b_layout.addWidget(button)
    button.setFlat(True)
    return button

appetizersb = menu_button('Appetizers')
appetizersb.setStyleSheet('''border:2px solid red; color:red; font-size:18px;
 background-color: rgb(238, 230, 238); border-radius:5px; width:250px; margin:0px 20px;height:30; ''')
soups_and_saladsb = menu_button('Soups_and_salads')
rice_itemsb = menu_button('Rice_items')
breads_rotisb = menu_button('Breads_rotis')
special_curriesb = menu_button('Special_curries')
side_dishesb = menu_button('Side_dishes')
desertsb = menu_button('Deserts')
drinksb = menu_button('Drinks')

appetizers = Items(Appetizers)
soups_and_salads = Items(Soups_and_salads)
rice_items = Items(Rice_items)
breads_rotis = Items(Breads_rotis)
special_curries = Items(Special_curries)
side_dishes = Items(Side_dishes)
deserts = Items(Deserts)
drinks = Items(Drinks)

categories = {'appetizers':appetizers,'soups_and_salads':soups_and_salads,'rice_items':rice_items,
                  'breads_rotis':breads_rotis,'special_curries':special_curries,
                  'side_dishes':side_dishes,'deserts':deserts,'drinks':drinks}
buttons_dict = {'appetizers':appetizersb,'soups_and_salads':soups_and_saladsb,'rice_items':rice_itemsb,
                'breads_rotis':breads_rotisb,'special_curries':special_curriesb,
                'side_dishes':side_dishesb,'deserts':desertsb,'drinks':drinksb}

def change_category(category):
    global curr_cat,buttons_dict,buttons
    category = category.lower()
    categories[curr_cat].hide()
    window_layout.addWidget(categories[category],2,2,3,4)
    categories[category].show()
    buttons_dict[curr_cat].setStyleSheet('''border:0px; color:rgb(0,0,50); font-size:18px;
 background-color: transparent; border-radius:5px; width:250px; margin:0px 20px;height:30; ''')
    buttons_dict[category].setStyleSheet('''border:2px solid red; color:red; font-size:18px;
 background-color: rgb(238, 230, 238); border-radius:5px; width:250px; margin:0px 20px;height:30; ''')
    curr_cat = category

separator = QFrame()
separator.setFrameShape(QFrame.VLine)
separator.setFrameShadow(QFrame.Sunken)
separator.setLineWidth(10)
separator.setStyleSheet("color: #FF0000;")

window_layout.addWidget(title, 0, 0, 1, 6)
window_layout.addWidget(tab1, 1, 0,1,3)
window_layout.addWidget(tab2, 1, 3,1,3)
window_layout.addWidget(buttons, 2, 0, 3, 1)
window_layout.addWidget(separator, 2, 1, 3, 1)
window_layout.addWidget(appetizers, 2, 2, 3, 4)

window.setLayout(window_layout)
window.show()
app.exec()