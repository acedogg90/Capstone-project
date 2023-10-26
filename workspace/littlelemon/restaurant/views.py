from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def restaurant(request):
    return render(request, 'restaurant_template.html')

# Declare two classes: MenuItemView – inheriting the rest_framework.generics.ListCreateView class. It handles the POST and GET method calls. SingleMenuItemView – inherits the RetrieveUpdateAPIView and DestroyAPIView classes both imported from the rest_framework.generics module. This class is responsible for processing GET, PUT and DELETE method calls.
class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
