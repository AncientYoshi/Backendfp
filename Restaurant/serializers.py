# serializers.py

from rest_framework import serializers
from .models import Menu, Booking  # Import your Menu model here

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Inventory', 'Price']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
