# Generated by Django 5.0.6 on 2024-08-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_appetizers_availability_breads_rotis_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders_placed',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
