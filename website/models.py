from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Appetizers(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(null=True)
    img = models.CharField(max_length=30,null=True)
class Soups_salads(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
class Rice_items(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
class Breads_rotis(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
class Special_curries(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
class Side_dishes(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
class Deserts(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)
class Drinks(models.Model):
    item = models.CharField(max_length=30,null=True)
    price= models.IntegerField(default=100,null=True)
    img = models.CharField(max_length=30,null=True)

class Orders_placed(models.Model):
    name = models.CharField(max_length=25)
    items = models.TextField()
    time = models.CharField(max_length=25)
