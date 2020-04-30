
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
    path('Order/confirmOrder/<int:order_id>/<int:res_id>',views.confirmOrder, name='confirmOrder'),
    path('Order/cancelOrder/<int:order_id>/<int:res_id>',views.cancelOrder, name='cancelOrder'),
    path('Order/changeStateToDoing/<int:order_id>/<int:res_id>',views.changeStateToDoing, name='changeStateToDoing'),
    path('Order/changeStateToDone/<int:order_id>/<int:res_id>',views.changeStateToDone, name='changeStateToDone'),

    path('manageOrder/<int:id>/', views.manageOrder, name='manageOrder'),
    path('manageStateOrder/<int:id>/', views.manageStateOrder, name='manageStateOrder'),
    path('addNewOrder_list/<int:user_id>/<int:res_id>/<int:food_id>',views.addNewOrder_List,name='addNewOrder_List'),
    path('addOrder_list/<int:user_id>/<int:res_id>/<int:food_id>/<int:order_id>',views.addOrder_List,name='addOrder_List'),
    path('selectFood/<int:id>/<int:order_id>',views.selectFood,name='selectFood'),
    path('Order/createOrder/<int:order_id>/',views.createOrder, name='createOrder'),
    path('Order/deleteOrder/<int:order_id>/<res_id>',views.deleteOrder, name='deleteOrder'),
    path('Order/deleteOrderList/<int:id>/<int:order_id>/<int:list_no>',views.deleteOrderList, name='deleteOrderList'),
    path('Order/StateOrder/<int:user_id>',views.stateOrder,name='stateOrder')
    ]
