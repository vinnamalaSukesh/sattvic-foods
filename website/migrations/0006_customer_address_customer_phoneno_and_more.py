# Generated by Django 5.0.6 on 2024-07-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_orders_placed_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='phoneNo',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AddField(
            model_name='orders_placed',
            name='contactNo',
            field=models.CharField(default='', max_length=13),
        ),
    ]