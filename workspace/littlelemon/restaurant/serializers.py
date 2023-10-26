from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem, Booking

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# declare the MenuSerializer class that subclasses ModelSerializer.
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory"]

# declare the BookingSerializer class that subclasses ModelSerializer.
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["__all__"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["__all__"]