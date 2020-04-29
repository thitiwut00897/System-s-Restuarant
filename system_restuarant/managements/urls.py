
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login', views.my_login, name='login'),
    path('logout', views.my_logout, name='logout'),
    path('registerOwner',views.registerOwner,name='registerOwner'),
    path('registerCustomer',views.registerCustomer,name='registerCustomer'),
    path('profile/', views.profile, name='profile'),
    path('profile/editProfile', views.editProfile, name='editProfile'),
    path('profile/changePassword', views.changePassword, name='changePassword'),
    # menagement Restuarant&Menu
    path('restaurant/detailRestaurant/<int:id>/', views.detailRestaurant, name='detailRestaurant'),

    path('restaurant/', views.management, name='management'),
    path('restaurant/add/', views.addRestaurant, name='addRestaurant'),
    path('restaurant/edit/<int:id>/', views.editRestaurant, name='editRestaurant'),
    path('restautant/delete/<int:id>/',views.deleteRestaurant, name='deleteRestaurant'),
    path('restaurant/food/<int:id>/', views.managementFood, name='managementFood'),
    path('restaurant/food/<int:res_id>/add/', views.addFood, name='addFood'),
    path('restaurant/food/<int:res_id>/delete/<int:food_id>/', views.deleteFood, name='deleteFood'),
    path('restaurant/food/<int:res_id>/edit/<int:food_id>/',views.editFood, name='editFood'),

    path('manageOrder', views.manageOrder, name='manageOrder'),
    path('manageStateOrder', views.manageStateOrder, name='manageStateOrder'),
    path('Order/changeStateToDoing/<int:order_id>/',views.changeStateToDoing, name='changeStateToDoing'),
    path('Order/changeStateToDone/<int:order_id>/',views.changeStateToDone, name='changeStateToDone'),
    path('Order/confirmOrder/<int:order_id>/',views.confirmOrder, name='confirmOrder'),
    path('Order/cancelOrder/<int:order_id>/', views.cancelOrder, name='cancelOrder')
]
