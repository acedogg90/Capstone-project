from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from .models import MenuItem, Booking
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET'])

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def restaurant(request):
    return render(request, 'restaurant_template.html')

# Declare two classes: MenuItemView – inheriting the rest_framework.generics.ListCreateView class. It handles the POST and GET method calls. SingleMenuItemView – inherits the RetrieveUpdateAPIView and DestroyAPIView classes both imported from the rest_framework.generics module. This class is responsible for processing GET, PUT and DELETE method calls.
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    