from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import OrdersSerializer

def index(request):
    return render(request,'start.html')

def logout(request):
    request.session.flush()
    return redirect('/')

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
    name = request.session.get('name')
    if(name is None):
        return redirect('/login/')

    return render(request,'home.html',{'name':name})

def menu(request):
    name = request.session.get('name')
    if(name):
        Appetizers_data = Appetizers.objects.all().values('id','item', 'price', 'img','availability')
        Appetizers_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Appetizers_data]
        Soups_salads_data = Soups_salads.objects.all().values('id','item', 'price', 'img','availability')
        Soups_salads_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Soups_salads_data]
        Rice_items_data = Rice_items.objects.all().values('id','item', 'price', 'img','availability')
        Rice_items_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Rice_items_data]
        Breads_rotis_data = Breads_rotis.objects.all().values('id','item', 'price', 'img','availability')
        Breads_rotis_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Breads_rotis_data]
        Special_curries_data = Special_curries.objects.all().values('id','item', 'price', 'img','availability')
        Special_curries_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Special_curries_data]
        Side_dishes_data = Side_dishes.objects.all().values('id','item', 'price', 'img','availability')
        Side_dishes_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Side_dishes_data]
        Deserts_data = Deserts.objects.all().values('id','item', 'price', 'img','availability')
        Deserts_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Deserts_data]
        Drinks_data = Drinks.objects.all().values('id','item', 'price', 'img','availability')
        Drinks_data = [[item['id'],item['item'],item['price'],item['img'],item['availability']]  for item in Drinks_data]
        alldata = Appetizers_data + Soups_salads_data + Rice_items_data + Breads_rotis_data + Special_curries_data + Side_dishes_data + Deserts_data + Drinks_data
        alldata.sort(key=lambda x: x[1])
        return render(request,'menu.html',{'appetizers':Appetizers_data,'soups_salads':Soups_salads_data,'rice_items':Rice_items_data,'breads_rotis':Breads_rotis_data,'special_curries':Special_curries_data,'side_dishes':Side_dishes_data,'deserts':Deserts_data,'drinks':Drinks_data,'all':alldata,'name':name})
    else:
        return redirect('/login/')

def final(request):
    name = request.session.get('name')
    if(name is None):
        return redirect('/login/')
    names = Customer.objects.all().values('name')
    names = [name['name'] for name in names]

    nos = Customer.objects.all().values('phoneNo')
    nos = [no['phoneNo'] for no in nos]

    addresses = Customer.objects.all().values('address')
    addresses = [address['address'] for address in addresses]

    data = request.GET.get('items')
    name = request.session['name']
    index = names.index(name)
    no = nos[index]
    address = addresses[index]

    if(data != None):
        Or = Orders_placed()
        Or.name = name
        Or.items = data
        Or.contactNo = no
        Or.address = address
        Or.save()
    else:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
        'orders',
        {
            'type': 'send_message',
            'message': 'New order'
        }
    )
    return render(request,'final.html',{'name':name})

def get_Uname(request):
    uname = request.session.get('name')
    def ret_uname():
        return uname
    return ret_uname

class Orders(APIView):
    def get(self, request):
        orders = Orders_placed.objects.all().values('id','name','items','time','contactNo','address','status')
        user = get_Uname()
        print(user)
        filtered = []
        filtered = [order for order in orders if order['name'] == user]
        return JsonResponse({'orders': filtered}, safe=False)