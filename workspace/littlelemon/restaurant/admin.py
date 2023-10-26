from django.contrib import admin

# Register your models here.
#  register the Menu and Booking models with the admin site using the admin.site.register() method.
from .models import MenuItem, Booking

admin.site.register(MenuItem)
admin.site.register(Booking)
