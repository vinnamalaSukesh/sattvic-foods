from django.shortcuts import render,redirect
from .models import *
import json
import time

mails = Customer.objects.all().values('email')
mails = [email['email'] for email in mails]
names = Customer.objects.all().values('name')
names = [name['name'] for name in names]
nos = Customer.objects.all().values('phoneNo')
nos = [no['phoneNo'] for no in nos]
addresss = Customer.objects.all().values('address')
addresss = [address['address'] for address in addresss]

def index(request):
    name = request.session['name']
    if(name):
        request.session.flush()
    return render(request,'index.html')

logined = []
def login(request):
    global logined
    mails = Customer.objects.all().values('email')
    mails = [email['email'] for email in mails]
    passwords = Customer.objects.all().values('password')
    passwords = [password['password'] for password in passwords]
    names = Customer.objects.all().values('name')
    names = [name['name'] for name in names]
    if(request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if(email in mails):
            index = mails.index(email)
            if(passwords[index] == password):
                request.session['email'] = email
                request.session['name'] = names[index]
                return redirect('/Home/')
            else:
                return render(request,'login.html',{'error':'Invalid password'})
        else:
            return render(request,'login.html',{'error':'Invalid email'})
    else:
        return render(request,'login.html')

def register(request):
    emails = Customer.objects.all().values('email')
    emails = [email['email'] for email in emails]
    emails_json = json.dumps(emails)
    if(request.method == 'POST'):
        cus = Customer()
        cus.name = request.POST.get('name')
        cus.email = request.POST.get('email')
        cus.phoneNo = request.POST.get('tel')
        cus.password = request.POST.get('password')
        cus.address = request.POST.get('address')
        cus.save()
        return redirect('/login/')
    request.session['emails'] = emails_json
    return render(request,'register.html')

def home(request):
    name = request.session['name']
    if(name):
        return render(request,'home.html',{'name':name})
    else:
        return redirect('/login/')
def menu(request):
    name = request.session['name']
    if(name):
        Appetizers_data = Appetizers.objects.all().values('item', 'price', 'img')
        Appetizers_data = [[item['item'],item['price'],item['img']]  for item in Appetizers_data]
        Soups_salads_data = Soups_salads.objects.all().values('item', 'price', 'img')
        Soups_salads_data = [[item['item'],item['price'],item['img']]  for item in Soups_salads_data]
        Rice_items_data = Rice_items.objects.all().values('item', 'price', 'img')
        Rice_items_data = [[item['item'],item['price'],item['img']]  for item in Rice_items_data]
        Breads_rotis_data = Breads_rotis.objects.all().values('item', 'price', 'img')
        Breads_rotis_data = [[item['item'],item['price'],item['img']]  for item in Breads_rotis_data]
        Special_curries_data = Special_curries.objects.all().values('item', 'price', 'img')
        Special_curries_data = [[item['item'],item['price'],item['img']]  for item in Special_curries_data]
        Side_dishes_data = Side_dishes.objects.all().values('item', 'price', 'img')
        Side_dishes_data = [[item['item'],item['price'],item['img']]  for item in Side_dishes_data]
        Deserts_data = Deserts.objects.all().values('item', 'price', 'img')
        Deserts_data = [[item['item'],item['price'],item['img']]  for item in Deserts_data]
        Drinks_data = Drinks.objects.all().values('item', 'price', 'img')
        Drinks_data = [[item['item'],item['price'],item['img']]  for item in Drinks_data]
        alldata = Appetizers_data + Soups_salads_data + Rice_items_data + Breads_rotis_data + Special_curries_data + Side_dishes_data + Deserts_data + Drinks_data
        alldata.sort()
        return render(request,'menu.html',{'appetizers':Appetizers_data,'soups_salads':Soups_salads_data,'rice_items':Rice_items_data,'breads_rotis':Breads_rotis_data,'special_curries':Special_curries_data,'side_dishes':Side_dishes_data,'deserts':Deserts_data,'drinks':Drinks_data,'all':alldata,'name':name})
    else:
        return redirect('/login/')

def final(request):
    data = request.GET.get('items')
    index = names.index(logined)
    no = nos[index]
    address = addresss[index]
    name = request.session['name']
    if(data != None):
        Or = Orders_placed()
        Or.name = logined
        Or.items = data
        Or.contactNo = no
        Or.address = address
        Or.save()
    return render(request,'final.html',{'name':name})
