
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.management, name='management'),
    path('restaurant/add/', views.addRestaurant, name='addRestaurant'),
    path('restaurant/food/add/<int:id>/', views.addFood, name='addFood'),
    path('restautant/delete/<int:id>/', views.deleteRestaurant, name='deleteRestaurant'),
    path('restaurant/food/delete/<int:id>/', views.deleteFood, name='deleteFood')
    # path('restaurant/edit/<int:id>/', views.editRestaurant, name='editRestaurant')
]