# serializers.py

from rest_framework import serializers
from .models import Menu  # Import your Menu model here

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'Title', 'Inventory', 'Price']

