
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.my_login, name='login'),
    path('logout', views.my_logout, name='logout'),

    # menagement Restuarant&Menu
    path('restaurant/', views.management, name='management'),
    path('restaurant/add/', views.addRestaurant, name='addRestaurant'),
    # path('restaurant/homepage/', views.homepage, name='homepage'),
    path('restaurant/food/add/<int:id>/', views.addFood, name='addFood'),
    path('restautant/delete/<int:id>/',
         views.deleteRestaurant, name='deleteRestaurant'),
    # path('restaurant/detailRestaurant/<int:id>',
    #      views.detailRestaurant, name = 'detailRestaurant'),
    path('restaurant/food/<int:res_id>/delete/<int:food_id>/',
         views.deleteFood, name='deleteFood'),
    path('restaurant/edit/<int:id>/', views.editRestaurant, name='editRestaurant'),
    path('manageOrder', views.manageOrder, name='manageOrder')
    # path('restaurant/edit/<int:id>/', views.editRestaurant, name='editRestaurant'),
    # path('restaurant/food/edit/<int:id>/', views.editFood, name='editFood')
]
