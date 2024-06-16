from django.shortcuts import render,redirect
from .models import *
import json
import time

logined = ''
mails = Customer.objects.all().values('email')
mails = [email['email'] for email in mails]
names = Customer.objects.all().values('name')
names = [name['name'] for name in names]

Appetizers_list = Appetizers.objects.all().values('item')
Appetizers_prices = Appetizers.objects.all().values('price')
Appetizers_list = [item['item'] for item in Appetizers_list]
Appetizers_prices = [item['price'] for item in Appetizers_prices]
Appetizers_images = Appetizers.objects.all().values('img')
Appetizers_images = [img['img'] for img in Appetizers_images]
Appetizers = [[item,price,img] for item,price,img in zip(Appetizers_list,Appetizers_prices,Appetizers_images)]

Soups_salads_list = Soups_salads.objects.all().values('item')
Soups_salads_prices = Soups_salads.objects.all().values('price')
Soups_salads_list = [item['item'] for item in Soups_salads_list]
Soups_salads_prices = [item['price'] for item in Soups_salads_prices]
Soups_salads_images = Soups_salads.objects.all().values('img')
Soups_salads_images = [img['img'] for img in Soups_salads_images]
Soups_salads = [[item,price,img] for item,price,img in zip(Soups_salads_list,Soups_salads_prices,Soups_salads_images)]

Breads_rotis_list = Breads_rotis.objects.all().values('item')
Breads_rotis_list = [item['item'] for item in Breads_rotis_list]
Breads_rotis_prices = Breads_rotis.objects.all().values('price')
Breads_rotis_prices = [item['price'] for item in Breads_rotis_prices]
Breads_rotis_images = Breads_rotis.objects.all().values('img')
Breads_rotis_images = [img['img'] for img in Breads_rotis_images]
Breads_rotis = [[item,price,img] for item,price,img in zip(Breads_rotis_list,Breads_rotis_prices,Breads_rotis_images)]

Rice_items_list = Rice_items.objects.all().values('item')
Rice_items_list = [item['item'] for item in Rice_items_list]
Rice_items_prices = Rice_items.objects.all().values('price')
Rice_items_prices = [item['price'] for item in Rice_items_prices]
Rice_items_images = Rice_items.objects.all().values('img')
Rice_items_images = [img['img'] for img in Rice_items_images]
Rice_items = [[item,price,img] for item,price,img in zip(Rice_items_list,Rice_items_prices,Rice_items_images)]

Special_curries_list = Special_curries.objects.all().values('item')
Special_curries_list = [item['item'] for item in Special_curries_list]
Special_curries_prices = Special_curries.objects.all().values('price')
Special_curries_prices = [item['price'] for item in Special_curries_prices]
Special_curries_images = Special_curries.objects.all().values('img')
Special_curries_images = [img['img'] for img in Special_curries_images]
Special_curries = [[item,price,img] for item,price,img in zip(Special_curries_list,Special_curries_prices,Special_curries_images)]

Side_dishes_list = Side_dishes.objects.all().values('item')
Side_dishes_list = [item['item'] for item in Side_dishes_list]
Side_dishes_prices = Side_dishes.objects.all().values('price')
Side_dishes_prices = [item['price'] for item in Side_dishes_prices]
Side_dishes_images = Side_dishes.objects.all().values('img')
Side_dishes_images = [img['img'] for img in Side_dishes_images]
Side_dishes = [[item,price,img] for item,price,img in zip(Side_dishes_list,Side_dishes_prices,Side_dishes_images)]

Deserts_list = Deserts.objects.all().values('item')
Deserts_list = [item['item'] for item in Deserts_list]
Deserts_prices = Deserts.objects.all().values('price')
Deserts_prices = [item['price'] for item in Deserts_prices]
Deserts_images = Deserts.objects.all().values('img')
Deserts_images = [img['img'] for img in Deserts_images]
Deserts = [[item,price,img] for item,price,img in zip(Deserts_list,Deserts_prices,Deserts_images)]

Drinks_list = Drinks.objects.all().values('item')
Drinks_list = [item['item'] for item in Drinks_list]
Drinks_prices = Drinks.objects.all().values('price')
Drinks_prices = [item['price'] for item in Drinks_prices]
Drinks_images = Drinks.objects.all().values('img')
Drinks_images = [img['img'] for img in Drinks_images]
Drinks = [[item,price,img] for item,price,img in zip(Drinks_list,Drinks_prices,Drinks_images)]
all = Appetizers + Soups_salads + Rice_items + Breads_rotis + Special_curries + Side_dishes + Deserts + Drinks
all.sort()

def index(request):
    return render(request,'index.html')

def login(request):
    emails = Customer.objects.all().values('email')
    emails = [email['email'] for email in emails]
    emails = json.dumps(emails)
    passwords = Customer.objects.all().values('password')
    passwords = [password['password'] for password in passwords]
    passwords = json.dumps(passwords)
    return render(request,'login.html',{'emails':emails,'passwords':passwords})

def register(request):
    emails = Customer.objects.all().values('email')
    emails = [email['email'] for email in emails]
    emails_json = json.dumps(emails)
    if(request.method == 'POST'):
        cus = Customer()
        cus.name = request.POST.get('name')
        cus.email = request.POST.get('email')
        cus.tel = request.POST.get('tel')
        print(type(cus.tel),cus.tel)
        cus.password = request.POST.get('password')
        cus.save()
        return redirect('/login/')
    return render(request,'register.html',{'emails':emails_json})

def home(request):
    global logined
    names = Customer.objects.all().values('name')
    names = [name['name'] for name in names]
    email = request.POST.get('email')
    for i in range(len(mails)):
        if((mails[i] == email)):
            logined = names[i]
    return render(request,'home.html',{'name':logined.split(' ')[0]})

def menu(request):
    return render(request,'menu.html',{'appetizers':Appetizers,'soups_salads':Soups_salads,'rice_items':Rice_items,'breads_rotis':Breads_rotis,'special_curries':Special_curries,'side_dishes':Side_dishes,'deserts':Deserts,'drinks':Drinks,'all':all,'name':logined.split(' ')[0]})

def final(request):
    data = request.GET.get('items')
    if(data != None):
        Or = Orders_placed()
        Or.name = logined
        Or.items = data
        Or.save()
    return render(request,'final.html',{'name':logined.split(' ')[0]})
