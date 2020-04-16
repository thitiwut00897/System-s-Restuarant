from django.db import models
from enum import Enum
# Create your models here.

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Customer(models.Model):
    faculty = models.CharField(max_length=50)
    account_account_id = models.ForeignKey(Account,on_delete=models.CASCADE, primary_key=True)

class Owner(models.Model):
    picture_owner = models.ImageField(upload_to='uploads')
    account_account_id = models.ForeignKey(Account,on_delete=models.CASCADE, primary_key=True)

class StateChoices(Enum):
        QUEUING = "Queuing"
        DOING = "Doing"
        DONE = "Done"

class Order(models.Model):
    

    order_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10,choices=[(tag, tag.value) for tag in StateChoices],default=StateChoices.QUEUING)
    total_price = models.FloatField(max_length=10)
    date_time = models.DateTimeField(blank=True)
    customer_account_account_id = models.ForeignKey(Customer,on_delete=models.CASCADE, null=False)

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)
    
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    working_hours = models.TimeField(blank=True)
    picture_restaurant = models.ImageField(upload_to='uploads')
    restaurant_name = models.CharField(max_length=50)
    owner_account_account_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
    type_type_id = models.ForeignKey(Type,on_delete=models.CASCADE, null=False)

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='uploads')
    price = models.FloatField(max_length=10)
    restaurant_restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)

class Order_List(models.Model):
    list_no = models.AutoField(primary_key=True)
    unit = models.IntegerField()
    price = models.FloatField(max_length=50)
    order_order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_food_id = models.ForeignKey(Food, on_delete=models.CASCADE, null=False)

