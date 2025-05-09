from rest_framework import serializers
from .models import Orders_placed

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders_placed
        fields = '__all__'
