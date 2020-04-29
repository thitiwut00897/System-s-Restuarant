from django.contrib import admin
from classes.models import Customer, Food, Order, Order_List, Owner,Restaurant, Type
from django.contrib.auth.models import Permission

admin.site.register(Permission)

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)
