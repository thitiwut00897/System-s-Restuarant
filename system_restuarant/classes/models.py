from django.db import models
from enum import Enum
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    faculty = models.CharField(max_length=50)



class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    picture_owner = models.ImageField(
        upload_to='uploads')


class StateChoices(Enum):
    SENDREQUEST = "SendRequest"
    QUEUING = "Queuing"
    DOING = "Doing"
    DONE = "Done"





class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
    picture_restaurant = models.ImageField(
        upload_to='uploads')
    restaurant_name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, null=True, blank=True)
    types = models.ForeignKey(
        Type, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.restaurant_name if self.restaurant_name else ''

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10, choices=[(
        tag, tag.value) for tag in StateChoices], null=True, blank=True)
    total_price = models.IntegerField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,null=True)

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='uploads')
    price = models.IntegerField(max_length=10)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE)


class Order_List(models.Model):
    list_no = models.AutoField(primary_key=True)
    unit = models.IntegerField()
    price = models.IntegerField(max_length=50)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, null=True, blank=True)
