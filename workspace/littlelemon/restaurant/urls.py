#define URL route for index() view
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('menu/items/', views.MenuItemView.as_view()),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
