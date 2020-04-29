from django.contrib import admin
from classes.models import Customer, Food, Order, Order_List, Owner,Restaurant, Type
from django.contrib.auth.models import Permission

admin.site.register(Permission)

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Order_List)
admin.site.register(Owner)
admin.site.register(Type)