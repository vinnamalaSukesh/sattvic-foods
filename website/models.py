from django.db import models
from datetime import datetime
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=13,default='')
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=200,default='')
class Appetizers(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Soups_salads(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Rice_items(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Breads_rotis(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Special_curries(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Side_dishes(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Deserts(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Drinks(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
    availability = models.CharField(max_length=20,default='Available')
class Orders_placed(models.Model):
    name = models.CharField(max_length=25)
    items = models.TextField()
    time = models.DateTimeField()
    contactNo = models.CharField(max_length=13,default='')
    address = models.CharField(max_length=200,default='')
    status = models.CharField(max_length=20,default='pending')
    def save(self, *args, **kwargs):
        if not self.time:
            now = datetime.now()
            self.time = now.replace(microsecond=0)
        super().save(*args, **kwargs)