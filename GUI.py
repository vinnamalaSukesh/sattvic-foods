from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
conn = sqlite3.connect('./db.sqlite3')

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
    cursor = conn.cursor()
    cursor.execute(f'select * from website_{category}')
    category = cursor.fetchall()
    cursor.close()

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
        Cbox.addItem(i[4])
        L = ['Available','Unavailable','Delete']
        L.remove(i[4])
        Cbox.addItems(L)
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

    categories

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

    window_layout.removeWidget(categories[curr_cat])
    categories[curr_cat].hide()
    categories[curr_cat] = Items(curr_cat)
    window_layout.addWidget(categories[curr_cat],2,2,3,4)
    categories[curr_cat].show()
    cursor = conn.cursor()
    table = 'website_' + curr_cat
    cursor.execute(f'''SELECT * FROM {table} WHERE id = (SELECT MAX(id) FROM {table});''')
    item = cursor.fetchall()
    cursor.close()
    client.send_message({'message' :{'type' : 'new item','category':curr_cat,'item':item}})

def Save(id_,entries,cbox,p_layout):
    global curr_cat
    availability = cbox.currentText()
    if(availability == 'Delete'):
        name = entries[0].text()
        price = entries[1].text()
        path = entries[2].text()
        availability = cbox.currentText()
        print(availability)
        cursor = conn.cursor()
        table = 'website_' + curr_cat
        cursor.execute(f'''SELECT * FROM {table} WHERE id = {id_.text()}''')
        item = cursor.fetchall()
        cursor.close()

        cursor = conn.cursor()
        cursor.execute(f'''DELETE from {table} WHERE id = {id_.text()}''')
        conn.commit()
        cursor.close()
        cbox.parent().hide()
        p_layout.removeWidget(cbox.parent())
        client.send_message({'message':{'type':'delete','category':curr_cat,'item':item}})
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
        cursor = conn.cursor()
        table = 'website_' + curr_cat
        cursor.execute(f'''SELECT * FROM {table} WHERE id = {id_}''')
        item = cursor.fetchall()
        cursor.close()
        client.send_message({'message':{'type':'update','category':curr_cat,'item':item}})

def Edit(id_,entries,cbox):
    for entry in entries:
        entry.setReadOnly(False)
    entries[1].setFocus()
    cbox.setEnabled(True)

i = 0
def switch_item(id_):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE website_orders_placed
        SET status = ?
        WHERE id = ?
    ''', ('completed', id_))
    global pending_orders,comp_orders
    window_layout.removeWidget(pending_orders)
    pending_orders.hide()
    window_layout.removeWidget(comp_orders)
    comp_orders.hide()
    pending_orders,comp_orders = Orders_placed()
    window_layout.addWidget(pending_orders,3,0,2,6)
    pending_orders.show()

    conn.commit()
    cursor.close()

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
    cursor = conn.cursor()
    cursor.execute('select * from website_orders_placed')
    orders = cursor.fetchall()
    cursor.close()

    pending_orders = QGroupBox()
    global pending_layout,pending
    pending_layout = QGridLayout()
    pending_orders.setLayout(pending_layout)

    comp_orders = QGroupBox()
    comp_layout = QGridLayout()
    comp_orders.setLayout(comp_layout)

    pending = 0
    complete = 0
    for order in orders:
        if(order[6] == 'pending'):
            box = Pending_orders(order)
            y = pending % 4
            x = pending // 4
            pending_layout.addWidget(box,x,y)
            pending += 1
        else:
            box = Comp_orders(order)
            y = complete % 4
            x = complete // 4
            comp_layout.addWidget(box,x,y)
            complete += 1
    pending_scroll = QScrollArea()
    pending_scroll.setWidgetResizable(True)
    pending_scroll.setWidget(pending_orders)
    comp_scroll = QScrollArea()
    comp_scroll.setWidgetResizable(True)
    comp_scroll.setWidget(comp_orders)
    return pending_scroll,comp_scroll

def Pending_orders(order):
    box = QGroupBox()
    box_layout = QVBoxLayout()
    box.setLayout(box_layout)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setOffset(0, 0)
    shadow.setColor(QColor(0, 0, 0, 160))
    box.setGraphicsEffect(shadow)
    box.setFixedSize(295,350)

    title_layout = QHBoxLayout()
    id_ = QLabel(str(order[0]))
    id_.setStyleSheet('font-size:20px;border:2px solid red;border-radius:50%;')
    id_.setFixedSize(30,20)
    title_layout.addWidget(id_)
    t = 'Order placed at : ' + str(order[3].split(' ')[1])
    date = QLabel(t)
    date.setStyleSheet("font-size:18px;color:red;border:0px;")
    date.setFixedHeight(20)
    date.setAlignment(Qt.AlignRight | Qt.AlignTop)
    title_layout.addWidget(date)

    box_layout.addLayout(title_layout)
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
    box_layout.addWidget(scroll)

    t = 'Price : ' + str(price)
    label = QLabel(t)
    label.setFixedHeight(20)
    label.setStyleSheet('font-size:18px;color:red;')
    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    box_layout.addWidget(label)

    user = QPushButton('User details')
    user.setStyleSheet("border:1px solid white;font-size:18px;color:white;background-color:rgb(0,0,50);")
    user.setFixedHeight(25)
    user.clicked.connect(lambda checked,name=order[1],Cno=order[4],address=order[5]:show_info(name,Cno,address))
    box_layout.addWidget(user)

    comp = QPushButton('Completed')
    comp.clicked.connect(lambda _,id_=order[0]: switch_item(id_))

    comp.setStyleSheet("border:1px solid white;font-size:18px;color:white;background-color:rgb(0,50,0);")
    comp.setFixedHeight(25)
    box_layout.addWidget(comp)

    return box

def Comp_orders(order):
    box = QGroupBox()
    box_layout = QVBoxLayout()
    box.setLayout(box_layout)
    box.setFixedSize(295,350)
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setOffset(0, 0)
    shadow.setColor(QColor(0, 0, 0, 160))
    box.setGraphicsEffect(shadow)

    title_layout = QHBoxLayout()
    id_ = QLabel(str(order[0]))
    id_.setStyleSheet('font-size:20px;border:2px solid red;border-radius:50%;')
    id_.setFixedSize(30,20)
    title_layout.addWidget(id_)
    t = 'Order placed at : ' + str(order[3].split(' ')[1])
    date = QLabel(t)
    date.setStyleSheet("font-size:18px;color:red;border:0px;")
    date.setFixedHeight(20)
    date.setAlignment(Qt.AlignRight | Qt.AlignTop)
    title_layout.addWidget(date)

    box_layout.addLayout(title_layout)
    items = QGroupBox()
    items_layout = QVBoxLayout()
    items.setLayout(items_layout)
    items.setStyleSheet('border:0px;')
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(200)
    scroll.setWidget(items)
    scroll.setStyleSheet('border:0px;')

    price = 0
    for i in order[2].split(';'):
        item = i.split(',')
        t = item[0] + '  (' + item[2] + ')'
        label = QLabel(t)
        label.setStyleSheet("font-size:18px;")
        label.setFixedHeight(30)
        label.setStyleSheet('border:0px;;font-size:20px;')
        price += int(item[1])
        items_layout.addWidget(label)
    box_layout.addWidget(scroll)

    t = 'Price : ' + str(price)
    label = QLabel(t)
    label.setFixedHeight(20)
    label.setStyleSheet('font-size:18px;color:red;border:0px;')
    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    box_layout.addWidget(label)

    user = QPushButton('User details')
    user.setStyleSheet("border:1px solid white;font-size:18px;color:white;background-color:rgb(0,0,50);")
    user.setFixedHeight(30)
    user.clicked.connect(lambda checked,name=order[1],Cno=order[4],address=order[5]:show_info(name,Cno,address))
    box_layout.addWidget(user)

    return box
pending_orders,comp_orders= Orders_placed()

def switch_tab(tab):
    global pending_orders,comp_orders
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

appetizers = Items('appetizers')
soups_and_salads = Items('soups_salads')
rice_items = Items('rice_items')
breads_rotis = Items('breads_rotis')
special_curries = Items('special_curries')
side_dishes = Items('side_dishes')
deserts = Items('deserts')
drinks = Items('drinks')

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

def Order_update(order):
    order = order[0]
    global pending_layout,pending
    box = Pending_orders(order)
    y = pending % 4
    x = pending // 4
    pending += 1
    pending_layout.addWidget(box,x,y)

from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtWebSockets import QWebSocket
from PyQt5.QtWidgets import QApplication
import sys
import json

class Menu(QObject):
    def __init__(self):
        super().__init__()
        self.client = QWebSocket()
        self.client.error.connect(self.on_error)
        self.client.connected.connect(self.on_connected)
        self.client.disconnected.connect(self.on_disconnected)
        self.client.textMessageReceived.connect(self.on_message_received)
    def connect(self, url):
        self.client.open(QUrl(url))

    @pyqtSlot()
    def on_connected(self):
        print("WebSocket connected to Menu")

    @pyqtSlot()
    def on_disconnected(self):
        print("WebSocket disconnected to Menu")

    @pyqtSlot(str)
    def on_message_received(self, message):
        pass

    def send_message(self, message):
        self.client.sendTextMessage(json.dumps({'message': message}))

    @pyqtSlot('QAbstractSocket::SocketError')
    def on_error(self, error):
        print(f"WebSocket error: {error}")

class Order(QObject):
    def __init__(self):
        super().__init__()
        self.client = QWebSocket()
        self.client.error.connect(self.on_error)
        self.client.connected.connect(self.on_connected)
        self.client.disconnected.connect(self.on_disconnected)
        self.client.textMessageReceived.connect(self.on_message_received)

    def connect(self, url):
        self.client.open(QUrl(url))

    @pyqtSlot()
    def on_connected(self):
        print("WebSocket connected to order")

    @pyqtSlot()
    def on_disconnected(self):
        print("WebSocket disconnected to order")

    @pyqtSlot(str)
    def on_message_received(self, message):
        message = json.loads(message)
        if(message['message'] == 'New order'):
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM website_orders_placed
                WHERE id = (SELECT MAX(id) FROM website_orders_placed);''')
            order = cursor.fetchall()
            cursor.close()
            Order_update(order)

    def send_message(self, message):
        if self.client.state() == QWebSocket.ConnectedState:
            self.client.sendTextMessage(json.dumps({'message': 'New order'}))
        else:
            print("WebSocket is not connected")

    @pyqtSlot('QAbstractSocket::SocketError')
    def on_error(self, error):
        print(f"WebSocket error: {error}")

if __name__ == "__main__":
    client = Menu()
    client.connect("ws://localhost:5000/ws/Menu/")

    client1 = Order()
    client1.connect("ws://localhost:5000/ws/Order/")
app.exec()
